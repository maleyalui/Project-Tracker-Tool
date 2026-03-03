from models.user import User
from models.project import Project
from models.task import Task

def task_user_creation():
    user = User("Test", "test@gmail.com")
    assert user.name == "Test"


def test_project_add_task():
    project = Project("CLI", "Build tool", "2026-01-01")
    task = Task("Implement feature")
    project.add_task(task)
    assert len(project.tasks) == 1

def test_task_complete():
    task = Task("Test")
    task.mark_complete()
    assert task.status == "Complete"
