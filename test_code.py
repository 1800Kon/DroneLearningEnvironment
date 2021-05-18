import pytest

from Challenges.Challenge1_test.Challenge1 import *
from Challenges.Challenge2_test.Challenge2 import *
from Challenges.Challenge3_test.Challenge3 import *


def test_function1():
    assert (challenge1Test() == False)


def test_function2():
    assert (challenge2Test() == True)


def test_function3():
    assert (challenge3Test() == False)
