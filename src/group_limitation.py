from src.limitation import Limitation


class GroupLimitation:
    def __init__(self, limitations: list[Limitation]=None):
        self.limitations = limitations

    @property
    def limitations(self):
        return self._limitations

    @limitations.setter
    def limitations(self, limitations: list[Limitation]=None):
        self._limitations = limitations if limitations is not None else []

    def __iter__(self):
        return iter(self.limitations)

    def add_limitation(self, limitation: Limitation):
        self._limitations.append(limitation)

    def __add__(self, other):
        return GroupLimitation(self.limitations + other.limitations)

    def __str__(self):
        limitations = [ limitation.__str__() for limitation in self._limitations ]
        return f"Ограничения\n{'\n'.join(limitations)}"

