import pytest
import sympy

from src.fitness_function import FitnessFunction
from src.group_limitation import GroupLimitation
from src.system_limitations import SystemLimitations
from src.lagrange_function import LagrangeFunction
from src.limitation import Limitation


def test_get_lagrange_partial_derivatives_without_limitations():
    lagrange_function = LagrangeFunction(fitness_function=FitnessFunction('x1 + 2*x2'))
    system_limitations = SystemLimitations(lagrange_function)
    
    sut = system_limitations.get_lagrange_partial_derivatives()
    
    assert sut == {sympy.Symbol('x1') : sympy.sympify('1'),
                   sympy.Symbol('x2') : sympy.sympify('2')
                   }

@pytest.mark.parametrize('fitness_function, group_limitation, expected', [
    (FitnessFunction('x1 + x2 + x3'),
     GroupLimitation([Limitation('x1 + x2*x3 - x3 < 2')]),
     {sympy.Symbol('x1'): sympy.sympify('1 + λ1'),
      sympy.Symbol('x2'): sympy.sympify('1 + λ1*x3'),
      sympy.Symbol('x3'): sympy.sympify('1 + λ1*(x2 - 1)'),
      sympy.Symbol('λ1'): sympy.sympify('x1 + x2*x3 - x3 -2')
     }
     ),
    (FitnessFunction('x + y + z'),
     GroupLimitation([Limitation('x + x*y + z < 2')]),
     {sympy.Symbol('x'): sympy.sympify('1 + λ1*(y + 1)'),
      sympy.Symbol('y'): sympy.sympify('1 + λ1*x'),
      sympy.Symbol('z'): sympy.sympify('1 + λ1'),
      sympy.Symbol('λ1'): sympy.sympify('x + x*y + z - 2')
     }
    ),
])
def test_get_lagrange_partial_derivatives_with_limitations(fitness_function, group_limitation, expected):
    lagrange_function = LagrangeFunction(
        fitness_function=fitness_function,
        group_limitation=group_limitation
    )
    system_limitations = SystemLimitations(lagrange_function)

    sut = system_limitations.get_lagrange_partial_derivatives()

    assert sut == expected

@pytest.mark.parametrize('lagrange_function, expected', [
    (LagrangeFunction(fitness_function=FitnessFunction('x1 + x2*x3 - x3')),
     {sympy.Symbol('x1') : sympy.Symbol('v1'), sympy.Symbol('x2') : sympy.Symbol('v2'), sympy.Symbol('x3') : sympy.Symbol('v3')}),
    (LagrangeFunction(fitness_function=FitnessFunction('x + y*z - z')),
     {sympy.Symbol('x') : sympy.Symbol('v1'), sympy.Symbol('y') : sympy.Symbol('v2'), sympy.Symbol('z') : sympy.Symbol('v3')})
])
def test_creating_v_vars(lagrange_function, expected):
    system_limitation = SystemLimitations(lagrange_function)

    sut = system_limitation.get_v_vars()

    assert sut == expected

def test_creating_w_vars():
    lagrange_function = LagrangeFunction(fitness_function=FitnessFunction('x1 * x2 + 2 * x2'),
                                         group_limitation=GroupLimitation([Limitation(function='x1 - x2 > 1'),
                                                                           Limitation(function='x1 + 2*x2 < 2')
                                                                           ]))
    system_limitations = SystemLimitations(lagrange_function)

    sut = system_limitations.get_w_vars()

    assert sut == { sympy.Symbol('λ1') : sympy.Symbol('w1'), sympy.Symbol('λ2') : sympy.Symbol('w2') }