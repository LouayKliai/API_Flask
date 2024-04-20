from flask import Blueprint, request, jsonify
from Services.project_services import ProjectService

project_bp = Blueprint('project_bp', __name__)

@project_bp.route('/projects', methods=['POST'])
def create_project():
    data = request.json
    user_id = data.get('user_id')
    curriculum_id = data.get('curriculum_id')
    edge = data.get('edge', [])
    node = data.get('node', [])
    
    project_service = ProjectService()
    project_id = project_service.create_project(user_id, curriculum_id, edge, node)
    return jsonify({'project_id': project_id}), 201

@project_bp.route('/projects/<project_id>', methods=['GET'])
def get_project(project_id):
    project_service = ProjectService()
    project = project_service.get_project(project_id)
    if project:
        return jsonify(project), 200
    else:
        return jsonify({'error': 'Project not found'}), 404

@project_bp.route('/projects', methods=['GET'])
def get_all_projects():
    project_service = ProjectService()
    projects = project_service.get_all_projects()
    return jsonify(projects), 200

@project_bp.route('/projects/<project_id>', methods=['PUT'])
def update_project(project_id):
    data = request.json
    project_service = ProjectService()
    success = project_service.update_project(project_id, data)
    if success:
        return jsonify({'message': 'Project updated successfully'}), 200
    else:
        return jsonify({'error': 'Project not found'}), 404

@project_bp.route('/projects/<project_id>', methods=['DELETE'])
def delete_project(project_id):
    project_service = ProjectService()
    success = project_service.delete_project(project_id)
    if success:
        return jsonify({'message': 'Project deleted successfully'}), 200
    else:
        return jsonify({'error': 'Project not found'}), 404
