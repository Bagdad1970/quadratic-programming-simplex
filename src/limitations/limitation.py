import sympy


class Limitation:
    def __init__(self, inequality: str):
        """
        :param inequality: Функция
        """
        self.inequality = inequality

    @property
    def inequality(self):
        return self.__inequality

    @inequality.setter
    def inequality(self, inequality: str):
        if '=' in inequality and '<=' not in inequality and '>=' not in inequality:
            left, right = map(str.strip, inequality.split(sep='='))
            self.__inequality = sympy.Eq(sympy.sympify(left), int(right))
        else:
            self.__inequality = sympy.sympify(inequality)

    def limitation_type(self):
        return type(self.__inequality)

    def limitation_to_function(self):
        if isinstance(self.__inequality, sympy.Rel):
            return self.__inequality.lhs - self.__inequality.rhs
        return self.__inequality

    def __add__(self, other):
        return self.__inequality + other.__inequality

    def __str__(self):
        return f"{self.__inequality}"