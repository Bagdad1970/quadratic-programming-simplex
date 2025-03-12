import sympy


class FitnessFunction:
    def __init__(self, function: str):
        """
        :param function: Целевая функция
        """

        self.function = function

    @property
    def function(self):
        return self._function

    @function.setter
    def function(self, function: str):
        self._function = sympy.sympify(function)

    def __add__(self, other):
        return self.function + other.function