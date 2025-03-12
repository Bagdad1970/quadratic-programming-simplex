import re
import sympy

from src.lagrange_function import LagrangeFunction
from src.group_limitation import GroupLimitation

from src.partial_derivatives.lambda_partial_derivative import LambdaPartialDerivative
from src.partial_derivatives.variable_partial_derivative import VariablePartialDerivative


class SystemLimitations:
    def __init__(self, lagrange_function: LagrangeFunction):
        self.lagrange_function = lagrange_function
        self.standard_variables = self.get_standard_variables(self.lagrange_function.get_variables())
        self.lambda_variables = lagrange_function.lagrange_multipliers

        self.v_variables = self.get_v_vars()
        self.w_variables = self.get_w_vars()

        self.lagrange_partial_derivatives = self.get_lagrange_partial_derivatives()
        self.variable_partial_derivative = VariablePartialDerivative(partial_derivatives=self.lagrange_partial_derivatives,
                                                                     standard_vars=self.standard_variables,
                                                                     v_vars=self.v_variables)
        self.lambda_partial_derivative = LambdaPartialDerivative(partial_derivatives=self.lagrange_partial_derivatives,
                                                                 lambda_vars=self.lambda_variables,
                                                                 w_vars=self.w_variables)

    @staticmethod
    def is_lambda_variable_of_partial_derivative(derivative_var: sympy.Symbol):
        return re.match(r'λ\d', str(derivative_var))

    @staticmethod
    def is_standard_variable_of_partial_derivative(derivative_var: sympy.Symbol):
        return re.match(r'[a-z]\d*', str(derivative_var))

    def get_standard_variables(self, variables):
        return { variable for variable in variables if self.is_standard_variable_of_partial_derivative(variable) }

    def get_lagrange_partial_derivatives(self):
        lagrange_diff_dict = {}
        function = self.lagrange_function.lagrange_function
        for standard_variable in self.lagrange_function.get_variables():
            if self.is_lambda_variable_of_partial_derivative(standard_variable):
                lagrange_diff_dict[standard_variable] = sympy.diff(function, standard_variable)
            elif self.is_standard_variable_of_partial_derivative(standard_variable):
                lagrange_diff_dict[standard_variable] = sympy.diff(function, standard_variable)
        return lagrange_diff_dict

    def get_lambda_variables(self):
        return {variable for variable in self.lagrange_partial_derivatives.keys()
                if self.is_lambda_variable_of_partial_derivative(variable)
                }

    def get_v_vars(self) -> dict:
        v_variables = {}
        sorted_by_sum_ord_variables = sorted(self.standard_variables, key=lambda s: sum(ord(c) for c in str(s)))

        for i, var in enumerate(sorted_by_sum_ord_variables, start=1):
            v_variables[var] = sympy.Symbol(f"v{i}")
        return v_variables

    def get_w_vars(self) -> dict:
        w_variables = {}
        for i, lambda_variable in enumerate(self.lambda_variables, start=1):
            w_variables[lambda_variable] = sympy.Symbol(f"w{i}")
        return w_variables

    def all_limitations(self) -> GroupLimitation:
        return (self.variable_partial_derivative.all_limitations_for_variables() +
                self.lambda_partial_derivative.all_limitations_for_lambdas())

    def get_system_equations(self):
        return self.variable_partial_derivative.equations_with_variable_diffs()