from app import db

class Membro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)

    @staticmethod
    def validar_nome(nome):
        return 5 <= len(nome) <= 50
