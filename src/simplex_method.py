import scipy

from src.fitness_function import FitnessFunction
from src.group_limitation import GroupLimitation
from src.lagrange_function import LagrangeFunction
from src.system_limitations import SystemLimitations


def simplex_method(*, fitness_function_str: str, group_limitation: GroupLimitation, group_variable_limitation: GroupLimitation):
    fitness_function = FitnessFunction(fitness_function_str)
    lagrange_function = LagrangeFunction(fitness_function=fitness_function, group_limitation=group_limitation)

    system_limitations = SystemLimitations(lagrange_function)
    system_equations = system_limitations.get_new_system_equations()
    system_equation_limitation = system_limitations.get_new_system_limitation()

    for equation in system_equations:
        print(equation)

    artificial_equations = system_equations.create_system_with_artificial_vars()
    artificial_equations.nullify_constants_in_lhs()

    for equation in artificial_equations:
        print(equation)

    limitations = system_limitations.all_limitations()
    print(limitations)
    linear_fitness_function = artificial_equations.new_fitness_function()

    coefficients_linear_fitness = linear_fitness_function.function.as_coefficients_dict()
    print(coefficients_linear_fitness)

    print(linear_fitness_function.function)






