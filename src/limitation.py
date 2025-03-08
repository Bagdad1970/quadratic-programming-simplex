import sympy

class Limitation:
    def __init__(self, *, variables: sympy.symbols, coefficients: list[float]=None, comparison_sign: str, free_member: float):
        """
        :param variables: Кортеж, содержащий все переменные выражения
        :param coefficients: Коэффициенты переменных выражения
        :param comparison_sign: Знак сравнения
        :param free_member: Свободный член сравнения
        """

        self.variables = variables
        self.coefficients = coefficients
        self.comparison_sign = comparison_sign
        self._free_member = free_member

    @property
    def variables(self):
        return self._variables

    @variables.setter
    def variables(self, variables: sympy.symbols):
        if isinstance(variables, sympy.core.symbol.Symbol):
            self._variables = (variables,)
        else:
            self._variables = variables

    @property
    def coefficients(self):
        return self._coefficients

    @coefficients.setter
    def coefficients(self, coefficients: list[float]):
        if coefficients is not None:
            self._coefficients = coefficients
        else:
            self._coefficients = [1]

    @property
    def comparison_sign(self):
        return self._comparison_sign

    @comparison_sign.setter
    def comparison_sign(self, comparison_sign: str):
        self._comparison_sign = comparison_sign

    @property
    def free_member(self):
        return self._free_member

    def __str__(self):
        terms = [f"{self.coefficients[i]}*{self.variables[i]}" for i in range(min(len(self.variables), len(self.coefficients)))]
        return f"{' + '.join(terms)} {self.comparison_sign} {self.free_member}"  # не факт, что будет '+'