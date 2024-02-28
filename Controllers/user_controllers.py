
from flask import Blueprint, jsonify, request
from Services.user_services import UserService

user_bp = Blueprint('user_bp', __name__)
user_service = UserService()

@user_bp.route('/user', methods=['POST'])
def create_user():
    data = request.json
    user_id = user_service.create_user(data.get('firstname'), data.get('lastname'), data.get('age'), data.get('cin'), data.get('email'), data.get('password'))
    return jsonify({"user_id": str(user_id)}), 201

@user_bp.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"message": "User not found"}), 404

@user_bp.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    updated_count = user_service.update_user(user_id, data.get('firstname'), data.get('lastname'), data.get('age'), data.get('cin'), data.get('email'), data.get('password'))
    if updated_count > 0:
        return jsonify({"message": "User updated successfully"}), 200
    else:
        return jsonify({"message": "User not found"}), 404

@user_bp.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    deleted_count = user_service.delete_user(user_id)
    if deleted_count > 0:
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"message": "User not found"}), 404
