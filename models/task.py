class Task:

    id_counter = 1

    def __init__(self, title, assigned_to= None):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.title = title
        self.status = "Incomplete"
        self.assigned_to = assigned_to

    def mark_complete(self):
        self.status = "Complete"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "assigned_to":self.assigned_to
        }
    
    def __str__(self):
        return f"Task [{self.id}] {self.title} - {self.status}"