import sympy
from src.fitness_function import FitnessFunction
from src.group_limitation import GroupLimitation


class LagrangeFunction:
    def __init__(self, *, fitness_function: FitnessFunction, group_limitation: GroupLimitation=None):
        self.fitness_function = fitness_function
        self.group_limitation = group_limitation
        self.lagrange_multipliers = self.__create_lagrange_multipliers()
        self.lagrange_function = self.__create_lagrange_function()

    def __create_lagrange_multipliers(self):
        if not self.group_limitation:
            return []
        else:
            return [ sympy.symbols(f"λ{i + 1}") for i in range(len(self.group_limitation.limitations)) ]

    def __get_lagrange_terms_sum(self) -> list:
        if not self.lagrange_multipliers:
            return []

        lagrange_terms = [ self.lagrange_multipliers[i] * self.group_limitation.limitations[i].limitation_to_function()
                           for i in range(len(self.group_limitation.limitations))
                           ]
        return lagrange_terms

    def __create_lagrange_function(self):
        """Внутренний метод для создания функции Лагранжа"""
        return self.fitness_function.function + sum(self.__get_lagrange_terms_sum())

    def get_variables(self) -> set:
        return self.lagrange_function.free_symbols

    def __eq__(self, other):
        return self.lagrange_function == other.lagrange_function