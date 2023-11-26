from datetime import datetime


class DueDateError(Exception):
    pass


class Task():

    def __init__(self, title, description, assigned_to, due_date, status='PENDING'):
        self.title = title
        self.description = description
        self.assigned_to = assigned_to

        if due_date < datetime.now():
            raise DueDateError('Lo sentimos, la fecha no es válida.')

        self.due_date = due_date
        self.status = status

    #  coverage run -m pytest PyTest/test/test_task.py -v
    #  coverage report -m
    def done(self):
        self.status = 'DONE'

    def undone(self):
        self.status = 'PENDING'
