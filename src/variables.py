import sympy

class Variables:
    def __init__(self, variables: str):
       self.variables = variables

    @property
    def variables(self):
       return self._variables

    @variables.setter
    def variables(self, variables: str):
       var_symbols = sympy.symbols(variables.strip())
       if isinstance(var_symbols, sympy.core.symbol.Symbol):
           self._variables = (var_symbols,)
       else:
           self._variables = var_symbols

    def __str__(self):
        return f"{self._variables}"