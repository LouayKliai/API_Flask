from Models.document_model import Document

class DocumentService:
    def create_document(self, name, document_type,list_activity):
        document = Document(name=name,document_type=document_type,list_activity=list_activity)        
        document.save()
        return str(document.id)

    def get_document(self, document_id):
        document = Document.objects(id=document_id).first()
        return document.to_json() if document else None

    def update_document(self, document_id, data):
        document = Document.objects(id=document_id).first()
        if document:
            document.modify(**data)
            return True
        return False

    def delete_document(self, document_id):
        document = Document.objects(id=document_id).first()
        if document:
            document.delete()
            return True
        return False
