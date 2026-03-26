from models.task import Task


class TaskService:
    def __init__(self, data):
        self.data = data

    def create_task(self, project_title, title, assigned_to=None):
        """Create a task and assign it to a project."""
        project = self._find_project(project_title)

        if not project:
            raise ValueError(f"Project '{project_title}' not found.")

        task = Task(title, assigned_to)

        task_data = {
            "id": task.id,
            "title": task.title,
            "status": task.status,
            "assigned_to": task.assigned_to
        }

        project["tasks"].append(task_data)

        return task

    def mark_task_complete(self, project_title, task_id):
        """Mark a task as complete."""
        project = self._find_project(project_title)

        if not project:
            raise ValueError(f"Project '{project_title}' not found.")

        for task in project.get("tasks", []):
            if task["id"] == task_id:
                task["status"] = "complete"
                return task

        raise ValueError(f"Task ID '{task_id}' not found.")

    def get_tasks(self, project_title):
        """Get all tasks for a project."""
        project = self._find_project(project_title)

        if not project:
            raise ValueError(f"Project '{project_title}' not found.")

        return project.get("tasks", [])

    def _find_project(self, title):
        for user in self.data.get("users", []):
            for project in user.get("projects", []):
                if project["title"].lower() == title.lower():
                    return project
        return None