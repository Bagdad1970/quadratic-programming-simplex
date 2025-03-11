import sympy

from src.group_limitation import GroupLimitation
from src.limitation import Limitation
from src.system_equations import SystemEquations


class VariablePartialDerivative:

    def __init__(self, *, partial_derivatives: dict, standard_vars: set, v_vars: dict):
        self.partial_derivatives = partial_derivatives
        self.standard_vars = standard_vars
        self.v_vars = v_vars

    def limitations_with_variables(self):
        limitations_for_variables = GroupLimitation()

        for standard_var in self.standard_vars:
            limitations_for_variables.add_limitation(Limitation(f"{str(standard_var)} >= 0"))

        return limitations_for_variables

    def equations_with_variable_diffs(self):
        system_equations = SystemEquations()

        for standard_var in self.standard_vars:
            derivative_variable = self.partial_derivatives[standard_var]
            system_equations.add_equation(sympy.Eq(lhs=sympy.sympify(f"{str(derivative_variable)} - {self.v_vars[standard_var]}"), rhs=int(0)))
        return system_equations

    def limitations_with_variable_diffs(self) -> GroupLimitation:
        limitations_for_variable_diffs = GroupLimitation()

        for standard_var in self.standard_vars:
            limitations_for_variable_diffs.add_limitation(Limitation(f'{str(standard_var)} * {self.v_vars[standard_var]} = 0'))
        return limitations_for_variable_diffs

    def limitations_for_v(self):
        limitations_for_v_vars = GroupLimitation()

        for v_var in self.v_vars.values():
            limitations_for_v_vars.add_limitation(Limitation(f"{str(v_var)} >= 0"))
        return limitations_for_v_vars

    def all_limitations_for_variables(self):
        return (self.limitations_with_variables() +
                self.limitations_with_variable_diffs() +
                self.limitations_for_v())