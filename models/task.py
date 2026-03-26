from .base import BaseModel


class Task(BaseModel):
    def __init__(self, title, assigned_to=None):
        super().__init__()
        self.title = title
        self.status = "pending"
        self.assigned_to = assigned_to

    def mark_complete(self):
        self.status = "complete"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to,
        }

    def __repr__(self):
        return f"Task(id={self.id}, title='{self.title}', status='{self.status}')"