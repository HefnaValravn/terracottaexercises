from datetime import date, timedelta

import pytest
from calendars import CalendarStub
from tasks import Task, TaskList


def setup_function():
    global today
    today = date(2024, 6, 11)
    global tomorrow
    tomorrow = today + timedelta(days=1)
    global yesterday
    yesterday = today - timedelta(days=1)
    global calendar
    calendar = CalendarStub(today)
    global tasklist
    tasklist = TaskList(calendar)

def test_creation():
    
    #Assert
    assert len(tasklist.due_tasks) == 0
    assert len(tasklist.finished_tasks) == 0
    assert len(tasklist.overdue_tasks) == 0
    
    
    
def test_adding_task_with_due_day_in_future():
    #Arrange
    task = Task('do stuff', tomorrow)
    
    
    #Act
    tasklist.add_task(task)
    
    
    #Assert
    assert len(tasklist.due_tasks) == 1
    assert len(tasklist.overdue_tasks) == 0
    
    
def test_adding_task_with_due_day_in_past():
    #Arrange
    task = Task('do stuff', yesterday)
    
    #Act + Assert
    with pytest.raises(RuntimeError):
        tasklist.add_task(task)
    assert len(tasklist.due_tasks) == 0
    
    
def test_task_becomes_finished():
    #Arrange
    task = Task('do stuff', tomorrow)
    tasklist.add_task(task)
    
    #Act
    task.finished = True
    
    #Assert
    assert len(tasklist.due_tasks) == 0
    assert len(tasklist.finished_tasks) == 1