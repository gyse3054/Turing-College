#Testing with py.test
import pytest
from quadratic import quadratic
import cmath
import itertools
from hypothesis import given, assume, strategies as st



def test_quadratic():
    x1, x2 = quadratic(a = 8, b = 22, c = 15)
    assert 8*x1**2 + 22*x1 +15 == 0
    assert 8*x2**2 + 22*x2 +15 == 0

def test_quadratic_types():
    with pytest.raises(TypeError):
        quadratic(a = 8, b = 'hello', c = 15)

def test_torture_test():
    args = [10,0,1,18,-5,-1,0.5,-1,5]
    for a, b, c in itertools.permutations(args, 3):
        if a == 0:
            with pytest.raises(ZeroDivisionError):
                quadratic(a, b, c)
        else:
            x1, x2 = quadratic(a, b, c)
            assert cmath.isclose(a*x1**2 + b*x1 +c , 0.0, abs_tol = 0.001)


@given(
        st.floats(min_value=-1000, max_value=1000),
        st.floats(min_value=-1000, max_value=1000),
        st.floats(min_value=-1000, max_value=1000),
)

def test_quadratic_hypo(a, b, c):
    
    assume(abs(a) > 0.001)
    assume(abs(b) > 0.001)
    assume(abs(c) > 0.001)
    x1, x2 = quadratic(a,b,c)
    assert cmath.isclose(a*x1**2 + b*x1 +c , 0.0, abs_tol = 0.001)
    assert cmath.isclose(a*x2**2 + b*x2 +c , 0.0, abs_tol = 0.001)