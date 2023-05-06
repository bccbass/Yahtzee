import pytest

from  DiceClass import Dice
from card import valid_hand, yahtzee, sm_straight, lrg_straight, three_kind, four_kind, full_house

def test_dice():
    assert 0 < Dice.die() < 7

def test_valid_hand():
    assert valid_hand([1, 2, 3, 4, 5])
    assert not valid_hand(['cat', True, 6.1])

def test_three_kind():
    assert three_kind([1,2,1,3,1])
    assert three_kind([1,6,6,6,1])
    assert not three_kind([1,2,3,2,6])
    assert not three_kind([1,2,6,2,6])
    assert not three_kind([1,1,1,1,1])
    assert three_kind([1,1,1,3,3])

def test_four_kind():
    assert four_kind([3,3,3,3,6])
    assert not four_kind([3,3,3,6,6])
    assert not four_kind([3,3,6,6,6])
    assert not four_kind([1,2,3,4,5])

def test_full_house():
    assert full_house([1,1,1,6,6])
    assert not full_house([1,1,1,1,6])
    assert not full_house([1,2,3,4,5])

def test_sm_straight():
    assert sm_straight([1,4,2,2,3])
    assert sm_straight([6,6,3,5,4])
    assert sm_straight([1,2,3,4,6])
    assert not sm_straight([1,2,3,5,6])
    assert not sm_straight([1,3,5,6])

    


def test_lrg_straight():
    assert lrg_straight([1,2,3,4,5])
    assert not lrg_straight([1,2,3,4,6])
    assert not lrg_straight([1,2,4,5,6])
    assert not lrg_straight([1,1,1,2,2])


def test_yahtzee():
    assert yahtzee([1,1,1,1,1]) 
    assert not yahtzee([1,1,1,1,2])
    assert not yahtzee([1,2,3,4,5])
