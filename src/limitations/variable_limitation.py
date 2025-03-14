import sympy


class VariableLimitation:
    def __init__(self, inequality: str):
        self.__inequality = sympy.sympify(inequality)

    @property
    def inequality(self):
        return self.__inequality