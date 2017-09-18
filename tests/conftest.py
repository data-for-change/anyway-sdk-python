from anywaysdk import Anyway
from pytest import fixture


@fixture
def anyway():
    return Anyway()
