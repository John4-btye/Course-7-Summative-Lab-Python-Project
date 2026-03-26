from rich.console import Console
from rich.table import Table

console = Console()


def print_success(message):
    console.print(f"[bold green]{message}[/bold green]")


def print_error(message):
    console.print(f"[bold red]{message}[/bold red]")


def display_users(users):
    table = Table(title="Users")

    table.add_column("ID", justify="right")
    table.add_column("Name")
    table.add_column("Email")

    for user in users:
        table.add_row(str(user.get("id")), user.get("name"), user.get("email"))

    console.print(table)


def display_projects(projects):
    table = Table(title="Projects")

    table.add_column("ID", justify="right")
    table.add_column("Title")
    table.add_column("Description")
    table.add_column("Due Date")

    for project in projects:
        table.add_row(
            str(project.get("id")),
            project.get("title"),
            project.get("description"),
            str(project.get("due_date")),
        )

    console.print(table)


def display_tasks(tasks):
    table = Table(title="Tasks")

    table.add_column("ID", justify="right")
    table.add_column("Title")
    table.add_column("Status")

    for task in tasks:
        table.add_row(
            str(task.get("id")),
            task.get("title"),
            task.get("status"),
        )

    console.print(table)