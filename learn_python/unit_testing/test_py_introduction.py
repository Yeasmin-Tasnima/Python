# terminal command:
# py.test    'test all cases, which function name starts as test_* '
# py.test -v    ' -v for more details'
# py.test -v -rxs    ' -rxs for printing the reason'
# py.test -k multiply -v    'specify test case name with substring'
# py.test -m windows -v    'select test case according to its MARK TAG name'

import functions_for_test
import pytest
import sys


@pytest.mark.skip(reason='Not Necessary Now.')
def test_calc_addition():
    result = functions_for_test.calc_addition(2, 3)
    assert result == 5


@pytest.mark.skipif(sys.version_info > (3, 5), reason='Python Version > 3.5')
def test_calc_subtraction():
    result = functions_for_test.calc_subtraction(2, 3)
    assert result == -1


def test_calc_multiply():
    result = functions_for_test.calc_multiply(2, 3)
    assert result == 6


@pytest.mark.windows
def test_windows_1():
    assert True


@pytest.mark.windows
def test_windows_2():
    assert True


@pytest.mark.mac
def test_mac_1():
    assert True


@pytest.mark.mac
def test_mac_2():
    assert True
