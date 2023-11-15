class Todo:
    def __init__(self):
        self.todo_list = []
        
    def add(self, task):
        self.todo_list.append(task) 

    def show_todo(self):
        return self.todo_list 
    
    def mark_complete(self, task):
        self.todo_list.remove(task) 