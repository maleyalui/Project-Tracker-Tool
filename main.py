# main.py

import argparse
from rich import print
from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import load_data, save_data


# Load saved data
def load_users():
    raw_data = load_data()
    users = []

    for user_data in raw_data.get("users", []):
        user = User(user_data["name"], user_data["email"])

        for project_data in user_data.get("projects", []):
            project = Project(
                project_data["title"],
                project_data["description"],
                project_data["due_date"]
            )

            for task_data in project_data.get("tasks", []):
                task = Task(
                    task_data["title"],
                    task_data["assigned_to"],
                    task_data["status"]
                )
                project.add_task(task)

            user.add_project(project)

        users.append(user)

    return users


users = load_users()


# ---------------- USER COMMANDS ----------------

def add_user(args):
    user = User(args.name, args.email)
    users.append(user)
    save_data({"users" :[u.to_dict() for u in users]})
    print(f"[green]User added:[/green] {user}")


def list_users(args):
    if not users:
        print("[red]No users found.[/red]")
        return

    for user in users:
        print(user)


# ---------------- PROJECT COMMANDS ----------------

def add_project(args):
    for user in users:
        if user.name == args.user:
            project = Project(args.title, args.description, args.due_date)
            user.add_project(project)
            save_data([u.to_dict() for u in users])
            print("[green]Project added successfully![/green]")
            return

    print("[red]User not found.[/red]")


# ---------------- TASK COMMANDS ----------------

def add_task(args):
    for user in users:
        for project in user.projects:
            if project.title == args.project:
                task = Task(args.title, args.assigned_to)
                project.add_task(task)
                save_data([u.to_dict() for u in users])
                print("[green]Task added![/green]")
                return

    print("[red]Project not found.[/red]")


def complete_task(args):
    for user in users:
        for project in user.projects:
            for task in project.tasks:
                if task.title == args.title:
                    task.mark_complete()
                    save_data([u.to_dict() for u in users])
                    print("[green]Task marked complete![/green]")
                    return

    print("[red]Task not found.[/red]")


# ---------------- CLI SETUP ----------------

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers()

    # Add User
    parser_add = subparsers.add_parser("add-user")
    parser_add.add_argument("--name", required=True)
    parser_add.add_argument("--email", required=True)
    parser_add.set_defaults(func=add_user)

    # List Users
    parser_list = subparsers.add_parser("list-users")
    parser_list.set_defaults(func=list_users)

    # Add Project
    parser_project = subparsers.add_parser("add-project")
    parser_project.add_argument("--user", required=True)
    parser_project.add_argument("--title", required=True)
    parser_project.add_argument("--description", required=True)
    parser_project.add_argument("--due_date", required=True)
    parser_project.set_defaults(func=add_project)

    # Add Task
    parser_task = subparsers.add_parser("add-task")
    parser_task.add_argument("--project", required=True)
    parser_task.add_argument("--title", required=True)
    parser_task.add_argument("--assigned_to", required=True)
    parser_task.set_defaults(func=add_task)

    # Complete Task
    parser_complete = subparsers.add_parser("complete-task")
    parser_complete.add_argument("--title", required=True)
    parser_complete.set_defaults(func=complete_task)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()