# from curses.ascii import isdigit
import pytest
import student_names

def test_is_present():
    assert student_names.is_present("Eugene")
    
def test_nodigit():
    assert student_names