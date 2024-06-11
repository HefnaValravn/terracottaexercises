from datetime import date, timedelta

import pytest
from calendars import CalendarStub
from tasks import Task, TaskList


@pytest.fixture
def today():
    return date(2024, 6, 11)


@pytest.fixture
def tomorrow(today):
    return today + timedelta(days=1)


@pytest.fixture
def yesterday(today):
    return today - timedelta(days=1)


@pytest.fixture
def stub(today):
    return CalendarStub(today)


@pytest.fixture
def tasklist(stub):
    return TaskList(stub)


def test_creation(tasklist):
    #Arrange
    
    #Act
    
    #Assert
    assert len(tasklist.due_tasks) == 0
    assert len(tasklist.finished_tasks) == 0
    assert len(tasklist.overdue_tasks) == 0
    
    
    
def test_adding_task_with_due_day_in_future(tomorrow, tasklist):
    #Arrange
    task = Task('do stuff', tomorrow)
    
    
    #Act
    tasklist.add_task(task)
    
    
    #Assert
    assert len(tasklist.due_tasks) == 1
    assert len(tasklist.overdue_tasks) == 0
    
    
def test_adding_task_with_due_day_in_past(yesterday, tasklist):
    #Arrange
    task = Task('do stuff', yesterday)
    
    #Act + Assert
    with pytest.raises(RuntimeError):
        tasklist.add_task(task)
    assert len(tasklist.due_tasks) == 0
    
    
def test_task_becomes_finished(tomorrow, tasklist):
    #Arrange
    task = Task('do stuff', tomorrow)
    tasklist.add_task(task)
    
    #Act
    task.finished = True
    
    #Assert
    assert len(tasklist.due_tasks) == 0
    assert len(tasklist.finished_tasks) == 1