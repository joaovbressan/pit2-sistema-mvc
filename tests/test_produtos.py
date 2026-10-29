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
            db.session.commit()
        yield client

def login(client):
    return client.post('/login', data={'username': 'tester', 'senha': 'password'}, follow_redirects=True)

def test_cadastro_produto_valido(client):
    login(client)
    response = client.post('/produtos/novo', data={
        'nome': 'Teclado Mecanico',
        'categoria': 'Perifericos',
        'preco': '250.00',
        'quantidade_estoque': '15'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Teclado' in response.data

def test_impedir_preco_vazio_feedback_lucas(client):
    login(client)
    response = client.post('/produtos/novo', data={
        'nome': 'Mouse Sem Fio',
        'categoria': 'Perifericos',
        'preco': '',  # Preço em branco
        'quantidade_estoque': '5'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert 'obrigat'.encode('utf-8') in response.data or b'obrigatorio' in response.data