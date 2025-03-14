import pytest
import sympy

from src.fitness_function import FitnessFunction
from src.group_limitation import GroupLimitation
from src.lagrange_function import LagrangeFunction
from src.limitations.limitation import Limitation


@pytest.mark.parametrize('fitness_function, expected', [
    (FitnessFunction('x1 + x2**2 - 2*x3'),
     sympy.sympify('x1 + x2**2 - 2*x3')),
    (FitnessFunction('x + xy**2 - 2*z'),
     sympy.sympify('x + xy**2 - 2*z')),
    (FitnessFunction('x + xy**2 - 2*k'),
     sympy.sympify('x + xy**2 - 2*k'))
])
def test_creating_lagrange_function_without_limitations(fitness_function, expected):
    lagrange_function = LagrangeFunction(fitness_function=fitness_function)

    sut = lagrange_function.lagrange_function

    assert sut == expected

def test_creating_lagrange_function_with_limitations():
    fitness_function = FitnessFunction('x1 + x2**2 - 2*x3')
    group_limitation = GroupLimitation([Limitation('x1*x3 - x2 + 2*x3 < 1'),
                                        Limitation('x1*x3 - x2 > -1')
                                        ])

    sut = LagrangeFunction(fitness_function=fitness_function, group_limitation=group_limitation)

    assert sut.lagrange_function == sympy.sympify('x1 + x2**2 - 2*x3 + λ1*(x1*x3 - x2 + 2*x3 - 1) + λ2*(x1*x3 - x2 + 1)')