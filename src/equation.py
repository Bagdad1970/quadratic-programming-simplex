import sympy

class Equation(sympy.Equality):
    def __new__(cls, lhs, rhs=0, **kwargs):
        return super().__new__(cls, lhs, rhs, **kwargs)

    def sum_in_equation(self) -> float:
        terms = self.lhs.as_ordered_terms()
        return sum(term for term in terms if term.is_number)

    def replace_constants_sum_to_rhs(self):
        constant_sum = self.sum_in_equation()
        return Equation(self.lhs - constant_sum, self.rhs - constant_sum)

    def __eq__(self, other):
        if not isinstance(other, Equation):
            return False
        return self.lhs == other.lhs and self.rhs == other.rhs
