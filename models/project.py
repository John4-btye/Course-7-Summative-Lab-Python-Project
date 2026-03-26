from .base import BaseModel


class Project(BaseModel):
    def __init__(self, title, description="", due_date=None):
        super().__init__()
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": [t.to_dict() for t in self.tasks],
        }

    def __repr__(self):
        return f"Project(id={self.id}, title='{self.title}')"