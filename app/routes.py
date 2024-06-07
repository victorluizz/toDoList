from datetime import datetime
from models import Membro, Tarefa
from flask import request, jsonify, Blueprint
from app import db

bp_membros = Blueprint("membros", __name__)


@bp_membros.route('/membros', methods=['POST'])
def criar_membro():
    if 'nome' not in request.json or 'email' not in request.json:
        return jsonify({"message": "Dados incompletos!"}), 400

    nome = request.json['nome']
    email = request.json['email']

    if not Membro.validar_nome(nome):
        return jsonify({"message": "O nome deve ter o tamanho maior que 5 e menor 50 caracteres."}), 404

    if Membro.query.filter_by(email=email).first():
        return jsonify({"message": "O email inserido já está associado a outro membro!"}), 409

    novo_membro = Membro(nome=nome, email=email)
    db.session.add(novo_membro)
    db.session.commit()

    return jsonify({"message": "Membro criado com sucesso!"}), 200

@bp_membros.route('/membros', methods=['GET'])
def listar_membros():
    membros = Membro.query.all()
    return jsonify([{"id": m.id, "nome": m.nome, "email": m.email} for m in membros]), 200


bp_tarefas = Blueprint("tarefas", __name__)

prioridades = ['Baixa', 'Media', 'Alta']
@bp_tarefas.route('/tarefas', methods=['POST'])
def criar_tarefa():
    if 'nome' not in request.json:
        return jsonify({"message": "A tarefa não pode ser criada sem um nome!"}), 400

    nome = request.json['nome']
    descricao = request.json.get('descricao', '')
    prioridade = request.json.get('prioridade', 'Baixa')
    criador_id = request.json['criador_id']

    if prioridade not in prioridades:
        return jsonify({"message": f"Prioridade inválida. Opções válidas: {', '.join(prioridades)}"}), 400


    if not Tarefa.validar_nome(nome):
        return jsonify({"message": "O nome da tarefa deve ter tamamnho maior que 5 e menor que 50"}), 400

    if len(descricao) > 140:
        return jsonify({"message": "O nome da tarefa deve ter no máximo 140 caracteres"}), 400


    nova_tarefa = Tarefa(nome=nome, descricao=descricao, finalizada=False, prioridade=prioridade, criador_id=criador_id)

    db.session.add(nova_tarefa)
    db.session.commit()

    return jsonify({"message": "Tarefa criada com sucesso"}), 400


@bp_tarefas.route('/tarefas/<int:id>/concluir', methods=['PUT'])
def marcar_tarefa_concluida(id):
    tarefa = Tarefa.query.get(id)

    if not tarefa:
        return jsonify({"message": "Tarefa não encontrada"}), 400

    tarefa.finalizada = True
    tarefa.data_termino = datetime.utcnow()
    db.session.commit()

    return jsonify({"message:": "Tarefa atualizada com sucesso!"}), 200

@bp_tarefas.route('/lista_tarefas', methods=['GET'])
def listar_membros():
    tarefas = Tarefa.query.all()
    return jsonify([{"id": t.id, "nome": t.nome, "descricao": t.descricao, "prioridade": t.prioridade} for t in tarefas]), 200