from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from models.database import db
from models.produto import Produto

produto_bp = Blueprint('produto', __name__)

@produto_bp.route('/')
@produto_bp.route('/produtos')
@login_required
def listar_produtos():
    busca = request.args.get('busca', '').strip()
    categoria = request.args.get('categoria', '').strip()

    query = Produto.query
    if busca:
        query = query.filter(Produto.nome.ilike(f'%{busca}%'))
    if categoria:
        query = query.filter(Produto.categoria.ilike(f'%{categoria}%'))

    produtos = query.all()
    return render_template('produtos.html', produtos=produtos, busca=busca, categoria=categoria)

@produto_bp.route('/produtos/novo', methods=['POST'])
@login_required
def cadastrar_produto():
    nome = request.form.get('nome', '').strip()
    categoria = request.form.get('categoria', 'Geral').strip()
    preco_str = request.form.get('preco', '').strip()
    quantidade_str = request.form.get('quantidade_estoque', '0').strip()

    # Validação de backend rigorosa (Feedback Lucas - Impede campo de preço vazio)
    if not nome:
        flash('O nome do produto é obrigatório.', 'warning')
        return redirect(url_for('produto.listar_produtos'))

    if not preco_str:
        flash('O preço do produto é obrigatório e não pode ser deixado em branco.', 'danger')
        return redirect(url_for('produto.listar_produtos'))

    try:
        preco = float(preco_str.replace(',', '.'))
        if preco <= 0:
            flash('O preço deve ser um valor positivo superior a R$ 0,00.', 'danger')
            return redirect(url_for('produto.listar_produtos'))
    except ValueError:
        flash('Informe um formato numérico válido para o preço (Ex: 29.90).', 'danger')
        return redirect(url_for('produto.listar_produtos'))

    try:
        quantidade = int(quantidade_str)
        if quantidade < 0:
            flash('A quantidade em estoque não pode ser negativa.', 'danger')
            return redirect(url_for('produto.listar_produtos'))
    except ValueError:
        flash('A quantidade em estoque deve ser um número inteiro.', 'danger')
        return redirect(url_for('produto.listar_produtos'))

    novo_produto = Produto(nome=nome, categoria=categoria, preco=preco, quantidade_estoque=quantidade)
    db.session.add(novo_produto)
    db.session.commit()

    flash(f'Produto "{nome}" cadastrado com sucesso!', 'success')
    return redirect(url_for('produto.listar_produtos'))
