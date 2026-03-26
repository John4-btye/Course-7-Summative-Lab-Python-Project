import argparse

from utils.file_handler import load_data, save_data
from utils.formatter import (
    print_success,
    print_error,
    display_users,
    display_projects,
    display_tasks,
)

from services.user_service import UserService
from services.project_service import ProjectService
from services.task_service import TaskService


def main():
    parser = argparse.ArgumentParser(description="CLI Project Management Tool")
    subparsers = parser.add_subparsers(dest="command")

    # ---------------- USER COMMANDS ----------------

    add_user_parser = subparsers.add_parser("add-user")
    add_user_parser.add_argument("--name", required=True)
    add_user_parser.add_argument("--email", required=True)

    subparsers.add_parser("list-users")

    # ---------------- PROJECT COMMANDS ----------------

    add_project_parser = subparsers.add_parser("add-project")
    add_project_parser.add_argument("--user", required=True)
    add_project_parser.add_argument("--title", required=True)
    add_project_parser.add_argument("--description", default="")
    add_project_parser.add_argument("--due_date", default=None)

    list_projects_parser = subparsers.add_parser("list-projects")
    list_projects_parser.add_argument("--user", required=True)

    # ---------------- TASK COMMANDS ----------------

    add_task_parser = subparsers.add_parser("add-task")
    add_task_parser.add_argument("--project", required=True)
    add_task_parser.add_argument("--title", required=True)
    add_task_parser.add_argument("--assigned_to", default=None)

    list_tasks_parser = subparsers.add_parser("list-tasks")
    list_tasks_parser.add_argument("--project", required=True)

    complete_task_parser = subparsers.add_parser("complete-task")
    complete_task_parser.add_argument("--project", required=True)
    complete_task_parser.add_argument("--task_id", type=int, required=True)

    args = parser.parse_args()

    # Load data
    data = load_data()

    # Initialize services
    user_service = UserService(data)
    project_service = ProjectService(data)
    task_service = TaskService(data)

    try:
        # ---------------- USER LOGIC ----------------

        if args.command == "add-user":
            user = user_service.create_user(args.name, args.email)
            save_data(data)
            print_success(f"User '{user.name}' created.")

        elif args.command == "list-users":
            users = user_service.get_all_users()
            display_users(users)

        # ---------------- PROJECT LOGIC ----------------

        elif args.command == "add-project":
            project = project_service.create_project(
                args.user,
                args.title,
                args.description,
                args.due_date,
            )
            save_data(data)
            print_success(f"Project '{project.title}' added to user '{args.user}'.")

        elif args.command == "list-projects":
            projects = project_service.get_projects_by_user(args.user)
            display_projects(projects)

        # ---------------- TASK LOGIC ----------------

        elif args.command == "add-task":
            task = task_service.create_task(
                args.project,
                args.title,
                args.assigned_to,
            )
            save_data(data)
            print_success(f"Task '{task.title}' added to project '{args.project}'.")

        elif args.command == "list-tasks":
            tasks = task_service.get_tasks(args.project)
            display_tasks(tasks)

        elif args.command == "complete-task":
            task = task_service.mark_task_complete(
                args.project,
                args.task_id,
            )
            save_data(data)
            print_success(f"Task '{task['title']}' marked as complete.")

        else:
            parser.print_help()

    except ValueError as e:
        print_error(str(e))


if __name__ == "__main__":
    main()