import json
import os

from task import TaskManager

_DEFAULT = []
_FILE = 'tasks.json'

class Boot():
    def __init__(self):
        self._task_list = self._load()
        self._json_to_instance()

    def _load(self):
        if os.path.isfile(_FILE) and os.path.getsize(_FILE) > 0:
            try:
                with open(_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return _DEFAULT.copy()

        else:
            with open(_FILE, 'w', encoding='utf-8') as f:
                json.dump(_DEFAULT, f, indent=4)
                return _DEFAULT.copy()
            
    def save(self,):
        _task_list = TaskManager.get_tasks()
        print(_task_list)
        with open(_FILE, 'w', encoding='utf-8') as f:
                json.dump(_task_list, f, indent=4)

    def _json_to_instance(self):
        for task in self._task_list:
            TaskManager.add(task)