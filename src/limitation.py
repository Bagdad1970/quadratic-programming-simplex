import sympy

class Limitation:
    def __init__(self, variables: sympy.symbols, coefficients: list, free_member: float):
        self._variables = variables
        self._coefficients = coefficients
        self._free_member = free_member


