from .person import Person

class User(Person):

    id_counter = 1

    def __init__(self, name, email):
        super().__init__(name, email)
        self.id = User.id_counter
        User.id_counter += 1
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "projects":[p.to_dict() for p in self.projects]
        }
    def __str__(self):
        return f"User[{self.id}] {self.name} ({self.email})"