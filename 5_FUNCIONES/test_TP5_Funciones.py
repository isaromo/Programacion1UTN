import pytest
from functionsTP5 import prime_or_not, factorial, sum_digits

@pytest.mark.parametrize("number, prime", [
    (11, True),
    (15, False),
    (97, True),
    (40, False)
])

def test_prime_or_not(number, prime):
    assert prime_or_not(number) == prime

@pytest.mark.parametrize("n, f", [
    (3, 6),
    (4, 24),
    (2, 2),
])

def test_factorials(n, f):
    assert factorial(n) == f

@pytest.mark.parametrize("num, sum", [
    (888, 24),
    (123, 6),
    (911, 11),
])

def test_sum_digits(num, sum):
    assert sum_digits(num) == sum