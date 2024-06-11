from datetime import date


class Task:
    def __init__(self, description, due_date):
        self.__description = description
        self.__due_date = due_date
        self.__finished = False
        
        
        
    @property
    def description(self):
        return self.__description
    
    @property
    def due_date(self):
        return self.__due_date
    
    @property
    def finished(self):
        return self.__finished
    
    @finished.setter
    def finished(self, value):
        if value != True and value != False:
            raise Exception('Finished can only be set to True or False')
        self.__finished = value
        
    def __str__(self):
        return f'Description: {self.description} Due date: {self.due_date} Finished: {'yes' if self.finished else 'no'}'
    
    
    def __repr__(self):
        return self.__str__()
    
class TaskList:
    def __init__(self):
        self.__tasks = []

    def __len__(self):
        return len(self.__tasks)

    def add_task(self, task):
        if task.due_date < date.today():
            raise RuntimeError("New task shouldn't end before the current date")
        self.__tasks.append(task)

    @property
    def finished_tasks(self):
        return [task for task in self.__tasks if task.finished]

    @property
    def due_tasks(self):
        return [task for task in self.__tasks if not task.finished]

    @property
    def overdue_tasks(self):
        return [task for task in self.__tasks if not task.finished and task.due_date < date.today()]
    
    
    
task = Task('bake', date(2023, 10, 1))

print(task.description)

print(task.due_date)

print(task.finished)

task.finished = True

print(task.finished)


task2 = Task('bake', date(2025, 10, 1))
task3 = Task('bake', date(2026, 10, 1))
task4 = Task('bake', date(2027, 10, 1))
task5 = Task('bake', date(2028, 10, 1))
task6 = Task('bake', date(2029, 10, 1))


tasklist = TaskList()
tasklist.add_task(task2)
tasklist.add_task(task3)
tasklist.add_task(task4)
tasklist.add_task(task5)
tasklist.add_task(task6)

print(tasklist.due_tasks)