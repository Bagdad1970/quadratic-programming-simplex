import sympy

from src.limitation import Limitation


class GroupLimitations:
    def __init__(self, limitations: list[Limitation]=None):
        self.limitations = limitations

    @property
    def limitations(self):
        return self._limitations

    @limitations.setter
    def limitations(self, limitations: list[Limitation]=None):
        if limitations is None:
            self._limitations = []
        else:
            self._limitations = limitations

    def add_limitaion(self, limitation: Limitation):
        self._limitations.append(limitation)

    def __str__(self):
        limitations = [ limitation.__str__() for limitation in self._limitations ]
        return f"=====Система ограничений=====\n{'\n'.join(limitations)}\n============================="