from enum import Enum


class VertexType(Enum):
    CLIENT = "client"
    ROUTER = "router"
    SERVER = "server"


class Vertex:
    def __init__(self, value: int, v_type: VertexType):
        self.value = value
        self.v_type = v_type

    def __str__(self):
        return f"Vertex - {self.__repr__()}"

    def __repr__(self):
        return f"{self.value} ({self.v_type.value})"

    def __eq__(self, other):
        if type(self) is type(other):
            return self.v_type is other.v_type and self.value is other.value
        else:
            return False

    def __key(self):
        return self.v_type, self.value

    def __hash__(self):
        return hash(self.__key())
