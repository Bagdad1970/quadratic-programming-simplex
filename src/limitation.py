import sympy

class Limitation:
    def __init__(self, *, function: str, variables: sympy.symbols):
        """
        :param function: Функция
        :param variables: Переменные функции
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

    def limitation_to_function(self):
        if isinstance(self.function, sympy.Rel):
            return self.function.lhs - self.function.rhs
        return self.function

    def __add__(self, other):
        return self.function + other.function

    def __str__(self):
        return f"{self.function}"

limit = Limitation(function='x1 + x2 < 2', variables=sympy.symbols('x1 x2'))