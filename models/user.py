from .base import BaseModel


class User(BaseModel):
    def __init__(self, name, email):
        super().__init__()
        self._name = name
        self.email = email
        self.projects = []

    @property
    def name(self):
        return self._name

    def add_project(self, project):
        self.projects.append(project)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "projects": [p.to_dict() for p in self.projects],
        }

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}')"