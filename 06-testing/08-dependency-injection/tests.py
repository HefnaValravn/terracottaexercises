from datetime import date
from calendars import CalendarStub
from tasks import Task, TaskList


def test_task_becomes_overdue():
    today = date(2015, 7, 8)
    tomorrow = date(2015, 7, 9)
    nextWeek = date(2015, 7, 15)
    calendar = CalendarStub(today)
    task = Task('description', tomorrow)
    taskList = TaskList(calendar)

    taskList.add_task(task)
    calendar.today = nextWeek

    assert [task] == taskList.overdue_tasks
