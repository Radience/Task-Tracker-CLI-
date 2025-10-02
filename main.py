import argparse
import time
import task

class Command():
    def __init__(self):
        self._parser = argparse.ArgumentParser(prog='project', exit_on_error=False)
        self._subparsers = self._parser.add_subparsers(dest='command')
        self._add()
        self._update()
        self._delete()
        self._mark_in_progress()
        self._mark_done()
        self._show_tasks()

    def _add(self):
        _sm_parser = self._subparsers.add_parser('add')
        _sm_parser.add_argument('name')

    def _update(self):
        _sm_parser = self._subparsers.add_parser('update')
        _sm_parser.add_argument('id', type=int)
        _sm_parser.add_argument('description')

    def _delete(self):
        _sm_parser = self._subparsers.add_parser('delete')
        _sm_parser.add_argument('id', type=int)

    def _mark_in_progress(self):
        _sm_parser = self._subparsers.add_parser('mark-in-progress')
        _sm_parser.add_argument('id', type=int)

    def _mark_done(self):
        _sm_parser = self._subparsers.add_parser('mark-done')
        _sm_parser.add_argument('id', type=int)

    def _show_tasks(self):
        _sm_parser = self._subparsers.add_parser('list')
        _sm_parser.add_argument('status')

    def parse_args(self):
        return self._parser.parse_args()

commands = {
    'add' : lambda args: task.Task(args.name),
    'update' : lambda args: task.Task(args.name),
    'delete' : lambda args: task.Task(args.name),
    'mark-in-progress' : lambda args: task.Task(args.name),
    'mark-done' : lambda args: task.Task(args.name),
    'list' : lambda args: task.Task(args.name)
}

if __name__ == '__main__':
    try:
        cli = Command()
        args = cli.parse_args()
        commands[args.command](args)
    except Exception as e:
        print(type(e), e)