from array import array


class BitVector:
    def __init__(self, size: int):
        self.vector = bytearray((0,) * size)

    def set_to_one(self, *indices: int):
        for index in indices:
            self.vector[index] = 1

    def contain(self, *indices: int) -> bool:
        for index in indices:
            if not self.vector[index]:
                return False
        return True
