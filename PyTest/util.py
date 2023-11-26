def is_even(num):
    if not isinstance(num, int):
        raise TypeError("Invalid input type, only integers allowed")
    return num % 2 == 0
