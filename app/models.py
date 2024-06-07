from app import db


class Membro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)

    @staticmethod
    def validar_nome(nome):
        return 5 <= len(nome) <= 50

    def __repr__(self):
        return f'<Membro {self.nome}: {self.email}>'



class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(140), nullable=False)
    finalizada = db.Column(db.Boolean, nullable=False)
    data_termino = db.Column(db.DateTime)
    prioridade = db.Column(db.String(5), default='Baixa')
    criador_id = db.Column(db.Integer, db.ForeignKey('membro.id'), nullable=False)
    criador = db.relationship('Membro', backref=db.backref('tarefas', lazy=True))

    def __repr__(self):
        return f'<Tarefa {self.id}: {self.nome} - {self.prioridade.display}>'

    @staticmethod
    def validar_nome(nome):
        return 5 <= len(nome) <= 50

    @staticmethod
    def validar_descricao(descricao):
        return len(descricao) <= 140
