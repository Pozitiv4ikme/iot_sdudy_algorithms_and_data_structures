class Edge:
    def __init__(self, from_v: int, to_v: int, e_weight: int):
        self.from_v = from_v
        self.to_v = to_v
        self.e_weight = e_weight

    def __str__(self):
        return f"from {self.from_v} to {self.__repr__()} with weight {self.e_weight}"

    def __repr__(self):
        return f"{self.to_v}"

    def __eq__(self, other):
        if type(self) is type(other):
            return (self.from_v is other.from_v
                    and self.to_v is other.to_v
                    and self.e_weight is other.e_weight)
        else:
            return False

    def __key(self):
        return self.from_v, self.to_v, self.e_weight

    def __hash__(self):
        return hash(self.__key())
