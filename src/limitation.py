import sympy


class Limitation:
    def __init__(self, function: str):
        """
        :param function: Функция
        """

        self.function = function

    @property
    def function(self):
        return self._function

    @function.setter
    def function(self, function: str):
        if '=' in function and '<=' not in function and '>=' not in function:
            left, right = map(str.strip, function.split(sep='='))
            self._function = sympy.Eq(sympy.sympify(left), int(right))
        else:
            self._function = sympy.sympify(function)

    def limitation_type(self):
        return type(self.function)

    def limitation_to_function(self):
        if isinstance(self.function, sympy.Rel):
            return self.function.lhs - self.function.rhs
        return self.function

    def __add__(self, other):
        return self.function + other.function

    def __str__(self):
        return f"{self.function}"