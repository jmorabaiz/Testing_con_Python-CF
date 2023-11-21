from datetime import datetime, timedelta
import pytest
from PyTest.task import Task, DueDateError


def is_available_to_skip():
    return True


@pytest.fixture
def username():
    # return 'Cody'
    print('>>> Ejecutamos el código antes de la prueba.')
    yield 'Cody'  # Ejecutar acciones antes o después, no tiene tanto sentido al ser clases.
    print('>>> Ejecutamos el código después de la prueba.')

@pytest.fixture
def password():
    return 'password'


def test_username(username):
    print(username)
    assert username == 'Cody'


def test_username_password(username, password):
    assert username == 'Cody'
    assert password == 'password'


class TestTask:

    @pytest.mark.news
    def test_task(self):
        assert True

    @pytest.mark.news
    @pytest.mark.parametrize('title, description, assigned_to, due_date',
                             [('Titulo 1', 'Descripción 1', 'User 1', datetime.now() + timedelta(days=1)),
                              ('Titulo 2', 'Descripción 2', 'User 2', datetime.now() + timedelta(days=2)),
                              ('Titulo 3', 'Descripción 3', 'User 3', datetime.now() + timedelta(days=3)),
                              ('Titulo 4', 'Descripción 4', 'User 4', datetime.now() + timedelta(days=4))])
    def test_new_task(self, title, description, assigned_to, due_date):
        # due_date = datetime.now() + timedelta(days=1)
        # task = Task('Title', 'Description', 'Juan', due_date)

        task = Task(title, description, assigned_to, due_date)
        # pytest PyTest/test/test_task.py::TestTask::test_new_task -v
        assert task.title == title
        assert task.description == description
        assert task.assigned_to == assigned_to
        assert task.due_date == due_date

    @pytest.mark.due_date
    @pytest.mark.errors
    def test_due_date_error(self):
        with pytest.raises(DueDateError):
            due_date = datetime.now() - timedelta(days=1)
            Task('Title', 'Description', 'Juan', due_date)

    @pytest.mark.due_date
    def test_due_date(self):
        due_date = datetime.now() + timedelta(days=1)
        task = Task('Title', 'Description', 'Juan', due_date)

        assert task.due_date > datetime.now()

    @pytest.mark.skip(reason='Lo sentimos, la prueba no cumple con los requerimientos.')
    def test_skip(self):
        pass

    @pytest.mark.skipif(is_available_to_skip(), reason='Lo sentimos, la prueba no cumple con los requerimientos.')
    def test_skip_if(self):
        pass
