from models.database import db

class Produto(db.Model):
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    categoria = db.Column(db.String(80), nullable=False, default='Geral')
    preco = db.Column(db.Float, nullable=False)  # Impetição de NOT NULL (Correção Feedback Lucas)
    quantidade_estoque = db.Column(db.Integer, nullable=False, default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'categoria': self.categoria,
            'preco': self.preco,
            'quantidade_estoque': self.quantidade_estoque
        }
