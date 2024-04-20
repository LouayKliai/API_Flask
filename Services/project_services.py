from Models.project_model import Project
from datetime import datetime,timezone

class ProjectService:
    def create_project(self, user_id, curriculum_id, edge, node):
        project = Project(
            userID=user_id,
            curriculumID=curriculum_id,
            edge=edge,
            node=node,
            updated_at=datetime.now(timezone.utc),
            created_at=datetime.now(timezone.utc)
        )
        project.save()
        return str(project.id)
    def get_project(self, project_id):
        project = Project.objects(id=project_id).first()
        return project

    def get_all_projects(self):
        return Project.objects()

    def update_project(self, project_id, project_data):
        project = Project.objects(id=project_id).first()
        if project:
            project.modify(updated_at=datetime.utcnow(), **project_data)
            return True
        return False

    def delete_project(self, project_id):
        project = Project.objects(id=project_id).first()
        if project:
            project.delete()
            return True
        return False
