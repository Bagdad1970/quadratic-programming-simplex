import sympy
from sympy.core import symbol

x1, x2, l = sympy.symbols('x1 x2 l')
f = 2*x1*x1 + 2*x1*x2 + 2*x2*x2 - 4*x1 - 6*x2 + l*x1 + 2*l*x2 - 2*l

def get_diff(function, variable: symbol):
    return sympy.diff(function, variable)

print("Частная производная по x:", get_diff(f, x1))
print("Частная производная по y:", get_diff(f, x2))
print("Частная производная по l:", get_diff(f, l))