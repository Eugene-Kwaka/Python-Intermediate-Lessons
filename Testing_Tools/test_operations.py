import pytest
import operations


def test_addition():
    assert operations.add(4,5) == 9
    
def test_subtraction():
    assert operations.sub(5,4) == 1
    