import pytest

from maths.vectors import *


def test_is_number_001():
    assert is_number(1) == True

def test_is_number_002():
    assert is_number(0) == True
    
def test_is_number_003():
    assert is_number(-1) == True


def test_is_number_004():
    assert is_number(9.324) == True

def test_is_number_005():
    assert is_number(-0.0) == True
    
def test_is_number_006():
    assert is_number(-1.99) == True


def test_is_number_007():
    assert is_number( '1') == False

def test_is_number_008():
    assert is_number( "1.2") == False

def test_is_number_009():
    assert is_number( "apple") == False
    
def test_are_numbers_001():
    assert are_numbers( 1,3) == True

def test_are_numbers_002():
    assert are_numbers( 1,3.99) == True
    
def test_are_numbers_003():
    assert are_numbers( 1,'3.99') == False

def test_are_numbers_004():
    assert are_numbers( ) == True   

def test_sum_numbers_001():
    assert sum_numbers(1,2) == 3


def test_sum_numbers_002():
    assert sum_numbers(1,1.99) == 2.99

def test_sum_numbers_003():
    assert sum_numbers(1,-1.99) == -0.99
    
        
def test_sum_vectors():
    assert sum_vectors( [1,2,4,8], [1,2,4,8]) == [2,4,8,16]
