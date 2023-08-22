from project import calc_rgdp
from project import calc_rgdp_growth
from project import calc_chain_rate
import pytest

def main():
    test_calc_rgdp()
    test_calc_rgdp_growth()
    test_calc_chain_rate()

def test_calc_rgdp():
    assert calc_rgdp({"apple":[1, 4]}, {"orange":[2, 3]}) == 3

def test_calc_rgdp_growth():
    assert calc_rgdp_growth(116, 100) == 1.16

def test_calc_chain_rate():
    assert calc_chain_rate(1.16, 1.05) == 1.10

if __name__ == "__main__":
    main()
