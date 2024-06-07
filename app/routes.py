from models import Membro
from flask import request, jsonify, Blueprint
from app import db

bp_membros = Blueprint("membros", __name__)

@bp_membros.route('/membros', methods=['POST'])
def criar_membro():

    print("Rota /membros POST acessada!")
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
