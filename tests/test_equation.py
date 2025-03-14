import sympy

from src.equation import Equation

def test_sum_of_constants_in_equation():
    equation = Equation(lhs=sympy.sympify('-7 + x1 + x2**2 - 2*y + 6'), rhs=int(2))

    sut = equation.sum_in_equation()

    assert sut == -1

def test_replace_constants_sum_to_rhs():
    equation = Equation(lhs=sympy.sympify('-7 + x1 + x2**2 - 2*y + 6'), rhs=int(2))

    sut = equation.replace_constants_sum_to_rhs()

    assert sut == Equation(lhs=sympy.sympify('x1 + x2**2 - 2*y'), rhs=int(3))
