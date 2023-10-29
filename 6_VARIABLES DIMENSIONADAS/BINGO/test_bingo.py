import pytest

from functions import bingo_row, bingo_column, check_other_columns

@pytest.mark.parametrize("card, res", [
    ([[0,1,2,3,4],[0,1,1,1,1],[0,1,1,1,1],[0,1,1,1,1],[0,1,1,1,1]], True)
])

def test_bingo_row(card,res):
    assert bingo_column(card) == res

