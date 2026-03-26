from models.project import Project


class ProjectService:
    def __init__(self, data):
        self.data = data

    def create_project(self, user_name, title, description="", due_date=None):
        """Create a project and assign it to a user."""
        projects = user.get("projects", [])
        new_id = max([p["id"] for p in projects], default=0) + 1

        project = Project(title, description, due_date)
        project.id = new_id
        user = self._find_user(user_name)

        if not user:
            raise ValueError(f"User '{user_name}' not found.")

        project_data = {
            "id": project.id,
            "title": project.title,
            "description": project.description,
            "due_date": project.due_date,
            "tasks": []
        }

        user["projects"].append(project_data)

        return project

    def get_projects_by_user(self, user_name):
        """Return all projects for a given user."""
        user = self._find_user(user_name)

        if not user:
            raise ValueError(f"User '{user_name}' not found.")

        return user.get("projects", [])

    def _find_user(self, name):
        for user in self.data.get("users", []):
            if user["name"].lower() == name.lower():
                return user
        return None