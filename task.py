import datetime
from enum import Enum
from status import Status

_size: int = 0
_task_list: list = []

class Task:
    def __init__(self, id = _size+1, description: str | None = None, status: Status | None = str(Status.todo), createdAt = str(datetime.datetime.now()), updatedAt = None):
        global _size
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        _size += 1

class TaskManager():
    
    @staticmethod
    def add(**kwargs):
        _task_list.append(Task(**kwargs))

    @staticmethod
    def update(id, description):
        for task in _task_list:
            if task.id == id:
                task.description = description
                task.updatedAt = str(datetime.datetime.now())
            else:
                print('Uknown id')

    @staticmethod
    def delete(id):
        for task in _task_list:
            if task.id == id:
                _task_list.remove(task)

    @staticmethod
    def set_status(status: Status):
        for task in _task_list:
            if task.id == id:
                task.status = status

    @staticmethod
    def get_tasks(status: Status | None = None):
        match(status):
            case Status.done:
                return([task.__dict__ for task in _task_list if task.status == Status.done])
            
            case Status.in_progress:
                return([task.__dict__ for task in _task_list if task.status == Status.in_progress])

            case Status.todo:
                return([task.__dict__ for task in _task_list if task.status == Status.todo])

            case _:
                return([task.__dict__ for task in _task_list])