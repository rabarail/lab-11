"""
Program: test_rotation_utils.py
Author: Rajani Baraili
Purpose: verifies the adjust_rotation() function from
         rotation_utils.py,handles positive rotations, negative rotations,
         non-numeric inputs, and various edge cases correctly.
Starter Code: rotation_utils.py provided by Gabriel Walters (October 27, 2025).
Date: April 6, 2026
"""
import pytest 
from rotation_utils import adjust_rotation


def test_positive_100():
    assert adjust_rotation(100) == 100

def test_positive_460():
    assert adjust_rotation(460) == 100

def test_positive_820():
    assert adjust_rotation(820) == 100 

def test_negative_100():
    assert adjust_rotation(-100) == 260

def test_negative_460():
    assert adjust_rotation(-460) == 260

def test_negative_820():
    assert adjust_rotation(-820) == 260


def test_non_numeric_raises_type_error():
    with pytest.raises(TypeError):
        adjust_rotation("not a number")
