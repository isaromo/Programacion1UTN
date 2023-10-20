import pytest
from functions_ejPower import sum_digits

@pytest.mark.parametrize("a, res", [
    (27, 9),
    (13, 4)
])

def test_main(a, res):
    assert sum_digits(a) == res