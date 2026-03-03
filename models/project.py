from .task import Task

class Project:

    id_counter = 1

    def __init__(self, title, description, due_date):
        self.id = Project.id_counter
        Project.id_counter += 1
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []

    def add_task(self,task: Task):
        self.tasks.append(task)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description":self.description,
            "description":self.due_date,
            "due_date": self.due_date
        }
    def __str__(self):
        return f"Project[{self.id}] {self.title} (Due: {self.due_date})"