# Docstring
# __doc__

def palindromo(sentence: str) -> bool:
    """
    Permite conocer si un str es o no un palindromo.

    :param sentence: string
    :return: bool
    :examples:

    >>> palindromo('Anita lava la tina')
    True

    >>> palindromo('CodigoFacilito')
    False

    >>> sentence = 'Oso'
    >>> palindromo(sentence)
    True
    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]

# In python shell you can use:
# 1. docstring = __import__("02-Docstring")
# 2. docstring.palindromo.__doc__ or help(docstring.palindromo)

# To run doctest in terminal run "python -m doctest 02-Docstring.py -v"
