import pytest

from PyTest.util import is_even


class Testme:

    def test_even(self):
        assert is_even(2) == True

    @pytest.mark.parametrize("num, res", zip([0, 1, 2, 3, 4, 5], [True, False, True, False, True, False]))
    def test_many(self, num, res):
        assert is_even(num) is res

    def test_exception(self):
        with pytest.raises(TypeError) as e:
            is_even("abc")
        assert e.value.args[0] == "Invalid input type, only integers allowed"

