import pytest

from polynomial import Polynomial
from polynomial import RationalPolynomial

def test_polynomial_eq():
    a = Polynomial.from_string("-4 + x^2")
    b = Polynomial.from_string("x^2 - 4")
    assert a == b

def test_polynomial_eq2():
    a = Polynomial.from_string("-4 + x^2")
    b = Polynomial.from_string("-4 - x^2")
    assert a != b

def test_polynomial_addition():
    a = Polynomial.from_string("1 + 7*x^2")
    b = Polynomial.from_string("-3 - x + 2*x^2")
    c = Polynomial.from_string("-2 - x + 9*x^2")
    assert a + b == c

def test_polynomial_addition2():
    a = Polynomial.from_string("1 + 7*x^2")
    b = Polynomial.from_string("-3 - x^2 + 2*x^3")
    c = Polynomial.from_string("-2 + 6*x^2 + 2*x^3")
    assert a + b == c

def test_polynomial_addition2():
    a = Polynomial.from_string("-3 - x^2 + 2*x^3")
    b = Polynomial.from_string("1 + 7*x^2")
    c = Polynomial.from_string("-2 + 6*x^2 + 2*x^3")
    assert a + b == c

def test_polynomial_addition3():
    a = Polynomial.from_string("-3 -x -7*x^2")
    b = Polynomial.from_string("1 + 7*x^2")
    c = Polynomial.from_string("-2 - x")
    assert a + b == c

def test_polynomial_subtraction():
    a = Polynomial.from_string("-2 + 6*x^2 + 2*x^3")
    b = Polynomial.from_string("-3 - x^2 + 2*x^3")
    c = Polynomial.from_string("1 + 7*x^2")
    assert a - b == c

def test_polynomial_subtraction2():
    a = Polynomial.from_string("-2 - x")
    b = Polynomial.from_string("1 + 7*x^2")
    c = Polynomial.from_string("-3 -x -7*x^2")
    assert a - b == c

def test_polynomial_multiplication():
    a = Polynomial.from_string("4")
    b = Polynomial.from_string("2 - x + 3*x^2")
    c = Polynomial.from_string("8 - 4*x + 12*x^2")
    assert a * b == c

def test_polynomial_multiplication2():
    a = Polynomial.from_string("3 - 2*x^2 + x^3")
    b = Polynomial.from_string("2 - x + 3*x^2")
    c = Polynomial.from_string("6 + 4*x^3 - 3*x + 5*x^2 - 7*x^4 + 3*x^5")
    assert a * b == c

def test_rp_eq():
    a = RationalPolynomial.from_string("(-4 + x^2)/(x+7)")
    b = RationalPolynomial.from_string("(x^2 - 4)/(7+x)")
    assert a == b

def test_rp_eq2():
    a = RationalPolynomial.from_string("(-4 + x^2)/(x+5)")
    b = RationalPolynomial.from_string("(x^2 - 4)/(7+x)")
    assert a != b

def test_rp_addition():
    a = RationalPolynomial.from_string("(1+x)/(x+2)")
    b = RationalPolynomial.from_string("(1*x+3)/(x+4)")
    c = RationalPolynomial.from_string("(2*x^ 2 + 10 +10*x)/(8+ 1*x^2+ 6*x)")
    assert a + b == c