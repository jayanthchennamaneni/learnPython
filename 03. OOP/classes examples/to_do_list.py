class ToDoList(object):
    """
    A class representing a to-do list with functionalities to add, remove, and clear tasks.
    """

    def __init__(self, tasks=None):
        """
        Initializes a ToDoList instance with an optional list of tasks.
        """
        if tasks is None:
            tasks = []
        self.tasks = tasks
    
    def add_task(self, task):
        """
        Adds a task to the to-do list, raising a ValueError if the task already exists.
        """
        if task in self.tasks:
            raise ValueError(f"{task} is already in the to-do list")
        self.tasks.append(task)
    
    def remove_task(self, task):
        """
        Removes a task from the to-do list, raising a ValueError if the task does not exist.
        """
        if task not in self.tasks:
            raise ValueError(f"{task} is not in the to-do list")
        self.tasks.remove(task)
        
    def clear_tasks(self):
        """
        Clears all the tasks from the to-do list.
        """
        self.tasks.clear()

a = ToDoList()
a.add_task("buying groceries")
a.add_task("call dad tomorrow")
print(a.tasks)
a.add_task("running")
a.remove_task("buying groceries")
print(a.tasks)
a.clear_tasks()
print(a.tasks)
