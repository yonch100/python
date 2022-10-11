import pytest

def fizzBuzz(value):
	return str(value)

def checkFizzBuzz(value, expectedRetVal):
    retVal = fizzBuzz(value)
    assert retVal == expectedRetVal

def test_returns1Whit1PassedIn():
    checkFizzBuzz(1 , "1")

def test_returns2Whit2PassedIn():
    checkFizzBuzz(2, "2")