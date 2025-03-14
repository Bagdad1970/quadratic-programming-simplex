from src.group_limitation import GroupLimitation
from src.limitations.limitation import Limitation

import src.simplex_method as simplex_method
from src.limitations.variable_limitation import VariableLimitation

group_limitation=GroupLimitation([Limitation('x1 + 2*x2 <= 2')])
group_variable_limitation = GroupLimitation([VariableLimitation('x1 >= 0'),
                                            VariableLimitation('x2 >= 0')]
                                           )

simplex_method.simplex_method(fitness_function_str='2*x1**2 + 2*x1*x2 + 2*x2**2 - 4*x1 - 6*x2',
                              group_limitation=group_limitation,
                              group_variable_limitation=group_variable_limitation
                              )