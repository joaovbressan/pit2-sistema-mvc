from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from models.usuario import Usuario

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        senha = request.form.get('senha')
        
        user = Usuario.query.filter_by(username=username).first()
        if user and user.check_senha(senha):
            login_user(user)
            return redirect(url_for('produto.listar_produtos'))
        
        # Mensagem clara, empática e recuperável (Feedback Mariana)
        flash('Credenciais incorretas. Por favor, verifique seu usuário e senha e tente novamente. Caso tenha esquecido suas credenciais, contate o suporte do sistema.', 'danger')
    
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você encerrou a sessão com segurança.', 'info')
    return redirect(url_for('auth.login'))
