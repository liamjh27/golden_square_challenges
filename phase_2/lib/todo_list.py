class Todo:
    def __init__(self):
        self.task_list = []

    def add(self, task):
        self.task_list.append(task)

    def complete(self):
        return [task for task in self.task_list if task.complete == True]
    

    def incomplete(self):
        return [task for task in self.task_list if task.complete == False]
    
    def give_up(self):
        for task in self.task_list:
            task.mark_complete()