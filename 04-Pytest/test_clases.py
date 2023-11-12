import pytest


class TestExample():

	def test_suma_dos_numeros(self):
		assert 10 + 10 == 20, 'Lo sentimos la suma no es correcta'


	def test_rest_dos_numeros(self):
		assert 10 - 10 == 0, 'Lo sentimos la resta no es correcta'
