#from TestDataGenerator.convertors import func
from TestDataGenerator.generators import schflds
import pytest

# def test_tuple_item():
#     # assert func(3) == 4
#     print(func(3))

def test_schflds():

    schm = {
        "id":{"provider":"uuid","kwargs":{}},
        "guestid":{"provider":"numbers.between","kwargs":{"minimum":10001,"maximum":10011}},
        "brandid":{"provider":"numbers.between","kwargs":{"minimum":15,"maximum":15}},
        "dinedate":{"provider":"datetime.date","kwargs":{"start":2017,"end":2018}},
        "covers":{"provider":"numbers.between","kwargs":{"minimum":1,"maximum":5}}
        }

    schm_list = list(schm.items())
    datt = schm_list[1]

    dat = schflds(datt)

    assert isinstance(dat[0], str) == True
    assert isinstance(dat[1], int) == True
