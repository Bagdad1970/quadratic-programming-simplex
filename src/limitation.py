import sympy

class Limitation:
    def __init__(self, *, function: str, variables: sympy.symbols):
        """
        :param variables: Кортеж, содержащий все переменные выражения
        :param coefficients: Коэффициенты переменных выражения
        :param comparison_sign: Знак сравнения
        :param free_member: Свободный член сравнения
        """

        self.function = function
        self.variables = variables

    @property
    def function(self):
        return self._function

    @function.setter
    def function(self, function: str):
        self._function = sympy.sympify(function)

    @property
    def variables(self):
        return self._variables

    @variables.setter
    def variables(self, variables: sympy.symbols):
        if isinstance(variables, sympy.core.symbol.Symbol):
            self._variables = (variables,)
        else:
            self._variables = variables

    def __str__(self):
        return f"{self.function}"