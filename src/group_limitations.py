from src.limitation import Limitation


class GroupLimitations:
    def __init__(self):
        self._limitations = []



    def add_limitaion(self, limitation: Limitation):
        self._limitations.append(limitation)
