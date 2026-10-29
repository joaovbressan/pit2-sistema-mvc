from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from models.database import db
from models.produto import Produto
from models.venda import Venda

venda_bp = Blueprint('venda', __name__)

@venda_bp.route('/vendas', methods=['GET', 'POST'])
@login_required
def gerenciar_vendas():
    if request.method == 'POST':
        produto_id = request.form.get('produto_id')
        qtd_str = request.form.get('quantidade', '1')

        try:
            quantidade = int(qtd_str)
            if quantidade <= 0:
                flash('A quantidade da venda deve ser de pelo menos 1 unidade.', 'warning')
                return redirect(url_for('venda.gerenciar_vendas'))
        except ValueError:
            flash('Quantidade informada é inválida.', 'danger')
            return redirect(url_for('venda.gerenciar_vendas'))

        produto = Produto.query.get(produto_id)
        if not produto:
            flash('Produto selecionado não existe.', 'danger')
            return redirect(url_for('venda.gerenciar_vendas'))

        if produto.quantidade_estoque < quantidade:
            flash(f'Estoque insuficiente! O produto "{produto.nome}" possui apenas {produto.quantidade_estoque} unidade(s) disponíveis.', 'danger')
            return redirect(url_for('venda.gerenciar_vendas'))

        # Baixa automática no estoque do banco relacional
        produto.quantidade_estoque -= quantidade
        valor_total = round(produto.preco * quantidade, 2)

        nova_venda = Venda(produto_id=produto.id, quantidade=quantidade, valor_total=valor_total)
        db.session.add(nova_venda)
        db.session.commit()

        flash(f'Venda de {quantidade}x "{produto.nome}" registrada com sucesso! Total: R$ {valor_total:.2f}', 'success')
        return redirect(url_for('venda.gerenciar_vendas'))

    vendas = Venda.query.order_by(Venda.data_venda.desc()).all()
    produtos = Produto.query.filter(Produto.quantidade_estoque > 0).all()
    return render_template('vendas.html', vendas=vendas, produtos=produtos)
