import pytest


class TestExample:

    @classmethod
    def setup_class(cls) -> None:
        print('>>> El método setup_class se ejecuta antes de todas las pruebas.')
        # pass

    @classmethod
    def teardown_class(cls) -> None:
        print('>>> El método teardown_class se ejecuta después de todas las pruebas.')
        # pass

    def setup_method(self):
        # print('>>> El método setup se ejecuta antes de cada prueba.')
        self.numero1 = 10
        self.numero2 = 20

    def teardown_method(self):
        # print('>>> El método teardown se ejecuta después de cada prueba.')
        pass

    def test_suma_dos_numeros(self):
        assert self.numero1 + self.numero2 == 30, 'Lo sentimos la suma no es correcta'

    def test_rest_dos_numeros(self):
        assert self.numero1 - self.numero2 == -10, 'Lo sentimos la resta no es correcta'


class TestExample2:

    def test_multiplicacion_dos_numeros(self):
        assert 2 * 10 == 20, 'Lo sentimos la suma no es correcta'
