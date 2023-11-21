# assert

if __name__ == '__main__':
    try:
        assert 5 == 10, 'Lo sentimos 5 no es igual a 10.'

        # Esto se puede hacer, pero no es recomendable.
        # No es pythonico, siempre hay que atender posibles errores
        # if not 5 == 10:
        #     raise AssertionError('Lo sentimos 5 no es igual a 10.')

        # print(">>> El programa continúa con su ejecución!")

    except AssertionError as error:
        print(error)
