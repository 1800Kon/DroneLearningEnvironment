import pytest

from Challenges.Challenge1_test.Challenge1 import *
from Challenges.Challenge2_test.Challenge2 import *
from Challenges.Challenge3_test.Challenge3 import *


def test_function1():
    assert (challenge1Test() == "hello world! This is a test to see if the docker container is going to make the code work")


'''def test_function2():
    assert (challenge2Test() == True)


def test_function3():
    assert (challenge3Test() == False) '''
