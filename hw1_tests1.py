import pytest

try:
    import polynomial
except:
    from Week1.polynomial import Polynomial, RationalPolynomial


# I put my .python files in folders corresponding to the week, so
# don't forget to change that back to whatever you have it to

# CHANGES: I just put in a bunch of tests for weird typing and stuff, that's all.

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

# Tests by Richard, don't be sad if they don't pass :(


def test_rp_eq():
    a = RationalPolynomial.from_string("(-4 + x^2)/(x+7)")
    b = RationalPolynomial.from_string("(x^2 - 4)/(7+x)")
    assert a == b

def test_rp_eq2():
    a = RationalPolynomial.from_string("(-4 + x^2)/(x+5)")
    b = RationalPolynomial.from_string("(x^2 - 4)/(7+x)")
    assert a != b

def test_rp_eq3():
    a = RationalPolynomial.from_string("(-4 + x^2)/(x+5)")
    b = RationalPolynomial.from_string("(-x^2 + 4)/(5+x)")
    assert a == -b

def test_rp_addition():
    a = RationalPolynomial.from_string("(1+x)/(x+2)")
    b = RationalPolynomial.from_string("(1*x+3)/(x+4)")
    c = RationalPolynomial.from_string("(2*x^ 2 + 10 +10*x)/(8+ 1*x^2+ 6*x)")
    assert a + b == c

def test_rp_addition2():
    a = RationalPolynomial.from_string("(1+x)/(x+2)")
    b = RationalPolynomial.from_string("(1*x+5)/(x+4)")
    c = RationalPolynomial.from_string("(2*x^ 2 + 10 +10*x)/(8+ 1*x^2+ 6*x)")
    assert a + b != c

def test_rp_subtraction():
    a = RationalPolynomial.from_string("(1+x)/(x+2)")
    b = RationalPolynomial.from_string("(1*x+3)/(x+4)")
    c = RationalPolynomial.from_string("-2/(8+ 1*x^2+ 6*x)")
    assert a - b == c

def test_rp_subtraction2():
    a = RationalPolynomial.from_string("(1+x)/(x+2)")
    b = RationalPolynomial.from_string("(1*x+17)/(x+4)")
    c = RationalPolynomial.from_string("-2/(8+ 1*x^2+ 6*x)")
    assert a - b != c

def test_rp_tozero():
    a = RationalPolynomial.from_string("(1+x)/(x+2)")
    b = RationalPolynomial.from_string("0/1")
    assert (a-a)==b

def test_rp_mult():
    a = RationalPolynomial.from_string("(1+2*x^2)/(4*x+8)")
    b = RationalPolynomial.from_string("(1+2*x^2)/(x+2)")
    c = RationalPolynomial.from_string("1/4")
    assert b*c == a

def test_rp_mult2():
    a = Polynomial.from_string("x^4+1")
    b = RationalPolynomial.from_string("(1+2*x^2)/(x+2)")
    assert b == b*(a/a)

def test_rp_mult3():
    a = RationalPolynomial.from_string("(x^4+3*x-1)/(-7*x^2+2*x-9)")
    b = RationalPolynomial.from_string("(1+2*x^2)/(x+2)")
    c = RationalPolynomial.from_string("(2*x^6 +x^4+6*x^3+3*x-2*x^2-1)/-(7*x^3+12*x^2+5*x+18)")
    assert a*b==c

def test_rp_mult4():
    a = RationalPolynomial.from_string("(x^4+3*x-1)/(-7*x^2+2*x-9)")
    b = RationalPolynomial.from_string("(1+2*x^2)/(x+2)")
    c = RationalPolynomial.from_string("(2*x^6 +x^4+6*x^3+3*x-2*x^2-1)/-(7*x^3+12*x^2+5*x+19)")
    assert a*b!=c

def test_rp_div():
    a = RationalPolynomial.from_string("(x^4+3*x-1)/(-7*x^2+2*x-9)")
    b = RationalPolynomial.from_string("(1+2*x^2)/(x+2)")
    c = RationalPolynomial.from_string("(2*x^6 +x^4+6*x^3+3*x-2*x^2-1)/-(7*x^3+12*x^2+5*x+18)")
    assert c/a==b

def test_rp_div2():
    a = RationalPolynomial.from_string("(x^4+3*x-1)/(-7*x^2+2*x-9)")
    b = RationalPolynomial.from_string("(1+2*x^2)/(x+2)")
    c = RationalPolynomial.from_string("(2*x^6 +x^4+6*x^3+3*x-2*x^2-1)/-(7*x^3+12*x^2+5*x+18)")
    assert a==c/b

def test_rp_div3():
    a = RationalPolynomial.from_string("(x^4+3*x-1)/(-7*x^2+2*x-9)")
    b = RationalPolynomial.from_string("(1+2*x^2)/(x+2)")
    c = RationalPolynomial.from_string("(2*x^6 +x^4+6*x^3+3*x-2*x^2-1)/-(7*x^3+12*x^2+5*x+10)")
    assert a!=c/b

def test_rp_neg():
    a = RationalPolynomial.from_string("1/1")
    b = RationalPolynomial.from_string("(1+2*x^2)/(x+2)")
    c = RationalPolynomial.from_string("(1+2*x^2)/(-1*x - 2)")
    assert (-a)*b == c

def test_rp_fromstr():
    a = RationalPolynomial.from_string("-(1+2*x^2)/-(x+2)")
    b = RationalPolynomial.from_string("(1+2*x^2)/(x+2)")
    assert a==b

def test_rp_fromstr2():
    a = RationalPolynomial.from_string("(1+2 *x^2)/- (x+2)")
    b = RationalPolynomial.from_string("  (1+2 *x^2)/(x+2)")
    assert a==(-b) and (-a)==b

def test_rp_fromstr3():
    a = RationalPolynomial.from_string("-(1 +2*x^2)/( x+2 )")
    b = RationalPolynomial.from_string("(1+2 *x^2)/-(x+2 ) ")
    assert a==b


