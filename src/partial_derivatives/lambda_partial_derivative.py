import sympy

from src.group_limitation import GroupLimitation
from src.limitations.limitation import Limitation
from src.system_equations import SystemEquations


class LambdaPartialDerivative:
    def __init__(self, *, partial_derivatives: dict, lambda_vars: set, w_vars: dict):
        self.partial_derivatives = partial_derivatives
        self.lambda_vars = lambda_vars
        self.w_vars = w_vars

    def limitations_with_lambdas(self):
        limitations_for_lambdas = GroupLimitation()

        for lambda_var in self.lambda_vars:
            limitations_for_lambdas.add_limitation(Limitation(f"{str(lambda_var)} >= 0"))
        return limitations_for_lambdas

    def equations_with_lambda_diffs(self):
        system_equations = SystemEquations()

        for lambda_var in self.lambda_vars:
            derivative_lambda = self.partial_derivatives[lambda_var]
            system_equations.add_equation(
                sympy.Eq(lhs=sympy.sympify(f"{str(derivative_lambda)} + {self.w_vars[lambda_var]}"), rhs=int(0)))
        return system_equations

    def limitations_with_lambdas_diffs(self):
        limitations_for_lambdas_diffs = GroupLimitation()

        for lambda_var in self.lambda_vars:
            limitations_for_lambdas_diffs.add_limitation(Limitation(f'{str(lambda_var)} * ({self.w_vars[lambda_var]}) = 0'))

        return limitations_for_lambdas_diffs

    def limitations_for_w(self):
        limitations_for_w_vars = GroupLimitation()

        for w_var in self.w_vars.values():
            limitations_for_w_vars.add_limitation(Limitation(f"{str(w_var)} >= 0"))
        return limitations_for_w_vars

    def all_limitations_for_lambdas(self):
        return (self.limitations_with_lambdas() +
                self.limitations_with_lambdas_diffs() +
                self.limitations_for_w())