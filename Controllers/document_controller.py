from flask import Blueprint, jsonify, request
from Services.document_services import DocumentService
from decrators import login_required

document_bp = Blueprint('document_bp', __name__)
document_service = DocumentService()

@document_bp.route('/document', methods=['POST'])
#@login_required
def create_document():
    data = request.get_json()
    document_id = document_service.create_document(data.get('name'), data.get('document_type'), data.get('list_activity'))
    return jsonify({"document_id": str(document_id)}), 201
    

@document_bp.route('/document/<document_id>', methods=['GET'])
#@login_required
def get_document(document_id):
    document = document_service.get_document(document_id)
    if document:
        return jsonify(document), 200
    else:
        return jsonify({'error': 'Document not found'}), 404


@document_bp.route('/document/<document_id>', methods=['PUT'])
#@login_required
def update_document(document_id):
    data = request.get_json()
    success = document_service.update_document(document_id, data)
    if success:
        return jsonify({'message': 'Document updated successfully'}), 200
    else:
        return jsonify({'error': 'Document not found'}), 404


@document_bp.route('/document/<document_id>', methods=['DELETE'])
#@login_required
def delete_document(document_id):
    success = document_service.delete_document(document_id)
    if success:
        return jsonify({'message': 'Document deleted successfully'}), 200
    else:
        return jsonify({'error': 'Document not found'}), 404