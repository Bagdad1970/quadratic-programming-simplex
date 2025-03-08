import sympy


class FitnessFunction:
    def __init__(self, *, variables: sympy.symbols, coefficients: list[float]):
        """
        Целевая функция имеет стандартизированный вид ДОПИСАТЬ

        :param coefficients: Коэффициенты составляющих целевой функции
        """

        self.variables = variables
        self.coefficients = coefficients

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
        terms = []  # Список для хранения слагаемых

        num_vars = len(self.variables)
        coef_index = 0

        # Квадратичные члены (x1**2, x2**2 и т. д.)
        for i in range(num_vars):
            terms.append(f"{self.coefficients[coef_index]}*{self.variables[i]}**2")
            coef_index += 1

        # Попарные произведения (x1*x2, x1*x3 и т. д.)
        for i in range(num_vars):
            for j in range(i + 1, num_vars):
                terms.append(f"{self.coefficients[coef_index]}*{self.variables[i]}*{self.variables[j]}")
                coef_index += 1

        # Линейные члены (x1, x2 и т. д.)
        for i in range(num_vars):
            terms.append(f"{self.coefficients[coef_index]}*{self.variables[i]}")
            coef_index += 1

        # Формируем строку
        return f"f(x) = {' + '.join(terms)}"

fitness_function1 = FitnessFunction(variables=sympy.symbols('x1 x2'), coefficients=[2, 2, 2, -4, -6])
print(fitness_function1)




