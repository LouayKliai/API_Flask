
from flask import Blueprint, jsonify, request
from Services.user_services import UserService

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/api/register', methods=['POST'])
def add_user_route():
    user_data = request.json
    firstname = user_data.get('firstname')
    lastname = user_data.get('lastname')
    age = user_data.get('age')
    cin = user_data.get('cin')
    email = user_data.get('email')
    password = user_data.get('password')

    if UserService.user_exists_by_email(email):
        return jsonify({'message': 'Un utilisateur avec cet e-mail existe déjà.'}), 400

    try:
        UserService.create_user(firstname, lastname, age, cin, email, password)
        return jsonify({'message': 'Utilisateur ajouté avec succès.'}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

@user_bp.route('/api/login', methods=['POST'])
def login_user_route():
    user_data = request.json
    email = user_data.get('email')
    password = user_data.get('password')

    user = UserService.login_user(email, password)
    if user:
        return jsonify({'message': 'Connexion réussie.', 'user': user.__dict__}), 200
    else:
        return jsonify({'message': 'Échec de la connexion. Vérifiez vos identifiants.'}), 401


