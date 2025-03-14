import sympy

from src.equation import Equation
from src.fitness_function import FitnessFunction


class SystemEquations:
    def __init__(self, equations: list[Equation]=None):
        self.equations = equations

    @property
    def equations(self):
        return self.__equations

    @equations.setter
    def equations(self, equations: list[Equation]):
        if equations is None:
            self.__equations = []
        else:
            self.__equations = equations

    def create_system_with_artificial_vars(self):
        new_system_equations = SystemEquations()
        for artificial_var_num, equation in enumerate(self.equations, start=1):
            equation_with_artificial_var = Equation(lhs=sympy.sympify(f"{str(equation.lhs)} + z{artificial_var_num}"), rhs=equation.rhs)
            new_system_equations.add_equation(equation_with_artificial_var)
        return new_system_equations

    def new_fitness_function(self):
        equations_solved_about_z = SystemEquations()
        for artificial_var_num, equation in enumerate(self.equations, start=1):
            artificial_var = sympy.Symbol(f'z{artificial_var_num}')
            equations_solved_about_z.add_equation(Equation(lhs=-1*(equation.lhs - artificial_var), rhs=artificial_var))

        sum_lhs = sum(equation.lhs for equation in equations_solved_about_z)
        return FitnessFunction(f"{sum_lhs}")

    def add_equation(self, equation):
        self.equations.append(equation)

    def nullify_constants_in_lhs(self) -> None:
        for i, equation in enumerate(self.equations):
            self.equations[i] = equation.replace_constants_sum_to_rhs()

    def __iter__(self):
        return iter(self.equations)

    def __add__(self, other):
        return SystemEquations(self.equations + other.equations)