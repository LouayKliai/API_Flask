from mongoengine import Document, ReferenceField
from .curriculum_model import Curriculum
from .document_model import Document

class CurriculumDocumentAssociation(Document):
    curriculum = ReferenceField(Curriculum)
    document = ReferenceField(Document)
