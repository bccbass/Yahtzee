import pytest

from Classes import Dice
from card import yahtzee, sm_straight, lg_straight, three_kind, four_kind, full_house


def test_dice():
    assert 0 < Dice.die() < 7


def test_three_kind():
    assert three_kind([1, 2, 1, 3, 1])
    assert three_kind([1, 6, 6, 6, 1])
    assert not three_kind([1, 2, 3, 2, 6])
    assert not three_kind([1, 2, 6, 2, 6])
    assert not three_kind([1, 1, 1, 1, 1])
    assert three_kind([1, 1, 1, 3, 3])
    assert three_kind([5, 5, 5, 3, 6])


def test_four_kind():
    assert four_kind([3, 3, 3, 3, 6])
    assert not four_kind([3, 3, 3, 6, 6])
    assert not four_kind([3, 3, 6, 6, 6])
    assert not four_kind([1, 2, 3, 4, 5])


def test_full_house():
    assert full_house([1, 1, 1, 6, 6])
    assert not full_house([1, 1, 1, 1, 6])
    assert not full_house([1, 2, 3, 4, 5])


def test_sm_straight():
    assert sm_straight([1, 4, 2, 2, 3]) == 'Small Straight'
    assert sm_straight([6, 6, 3, 5, 4]) == 'Small Straight'
    assert sm_straight([1, 2, 3, 4, 6]) == 'Small Straight'
    assert not sm_straight([1, 2, 3, 5, 6]) == 'Small Straight'
    assert not sm_straight([1, 3, 5, 6]) == 'Small Straight'


def test_lg_straight():
    assert lg_straight([1, 2, 3, 4, 5]) == 'Large Straight'
    assert not lg_straight([1, 2, 3, 4, 6]) == 'Large Straight'
    assert not lg_straight([1, 2, 4, 5, 6]) == 'Large Straight'
    assert not lg_straight([1, 1, 1, 2, 2]) == 'Large Straight'
    assert lg_straight([3, 2, 5, 4, 6]) == 'Large Straight'


def test_yahtzee():
    assert yahtzee([1, 1, 1, 1, 1]) == 'Yahtzee!'
    assert not yahtzee([1, 1, 1, 1, 2]) == 'Yahtzee!'
    assert not yahtzee([1, 2, 3, 4, 5]) == 'Yahtzee!'
