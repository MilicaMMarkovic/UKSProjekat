from django.db import models


class ProjectManager(models.Model):
    def create_project(self, name, description=""):
        project = self.create(name=name, description=description)
        return project
