import sys

print(sys.path)

from TestDataGenerator.convertors import func
import pytest

def test_tuple_item():
    # assert func(3) == 4
    print(func(3))

test_tuple_item()
