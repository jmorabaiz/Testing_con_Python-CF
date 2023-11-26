"""Este es el Docstring del módulo 02-Docstring."""

# Docstring
# __doc__


class User:
    """Permite representar un usuario"""

    def __init__(self, username: str, password: str) -> None:
        """
        Permite instanciar un objeto de tipo User.

        :param username: str
        :param password: str
        """

        self.username = username
        self.password = password


def palindromo(sentence: str) -> bool:
    """
    Permite conocer si un str es o no un palindromo.

    :param sentence: string
    :return: bool
    :examples:

    # >>> palindromo('Anita lava la tina')
    # True
    #
    # >>> palindromo('CodigoFacilito')
    # False
    #
    # >>> sentence = 'Oso'
    # >>> palindromo(sentence)
    # True
    # """

    # Se pasa a un archivo plano, ya que es lo correcto para correr estos test
    # python -m doctest test_Docstring.txt -v

    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]

# In python shell you can use:
# 1. from Docstring import palindromo, User
# 2. docstring.palindromo.__doc__ or help(docstring.palindromo)
# 3. docstring.__doc__ or docstring.User.__doc__ or docstring.User.__init__.__doc__
# 4. help(docstring.User.__init__) - Best option

# To run doctest in terminal run "python -m doctest test_Docstring.py -v"
