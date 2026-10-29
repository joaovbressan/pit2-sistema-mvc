import pytest
from app import create_app
from models.database import db
from models.produto import Produto
from models.usuario import Usuario

class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SECRET_KEY = 'test-key'

@pytest.fixture
def client():
    app = create_app(TestConfig)
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            user = Usuario(nome='Tester', username='tester')
            user.set_senha('password')
            db.session.add(user)
            
            p = Produto(nome='Cabo HDMI 2m', categoria='Acessórios', preco=30.00, quantidade_estoque=10)
            db.session.add(p)
            db.session.commit()
        yield client

def login(client):
    return client.post('/login', data={'username': 'tester', 'senha': 'password'}, follow_redirects=True)

def test_venda_com_baixa_de_estoque(client):
    login(client)
    response = client.post('/vendas', data={
        'produto_id': '1',
        'quantidade': '3'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    
    # Verificar baixa no estoque
    with client.application.app_context():
        p = Produto.query.get(1)
        assert p.quantidade_estoque == 7  # 10 - 3 = 7
