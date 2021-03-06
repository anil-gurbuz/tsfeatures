from tsfeatures import holt_parameters
from tsfeatures.utils_ts import WWWusage, USAccDeaths
from math import isclose

def test_holt_parameters_seasonal():
    z = holt_parameters((USAccDeaths, 12))
    assert isclose(len(z), 2)
    assert isclose(z['alpha'], 0.96, abs_tol=0.05)
    assert isclose(z['beta'], 0., abs_tol=0.01)

def test_holt_parameters_non_seasonal():
    z = holt_parameters((WWWusage, 1))
    print(z)
    assert isclose(len(z), 2)
    assert isclose(z['alpha'], 0.99, abs_tol=0.02)
    assert isclose(z['beta'], 0.99, abs_tol=0.02)
