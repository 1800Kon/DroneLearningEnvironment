import pytest

from Index import isHelloCorrect


def test_function():
    word = 'Hello World'
    assert (isHelloCorrect(word) == True)