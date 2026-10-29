from flask import Flask
from config import Config
from models.database import db
from models.usuario import Usuario
from flask_login import LoginManager

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Acesso restrito. Por favor, autentique-se para continuar.'
    login_manager.login_message_category = 'warning'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    from controllers.auth_controller import auth_bp
    from controllers.produto_controller import produto_bp
    from controllers.venda_controller import venda_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(produto_bp)
    app.register_blueprint(venda_bp)

    with app.app_context():
        db.create_all()
        # Seed usuário administrador padronizado
        if not Usuario.query.filter_by(username='admin').first():
            admin = Usuario(nome='João Victor Teixeira Bressan', username='admin')
            admin.set_senha('admin123')
            db.session.add(admin)
            db.session.commit()

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
