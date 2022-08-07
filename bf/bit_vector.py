
class BitVector:
    def __init__(self, size: int):
        self.vector = 0

    def add(self, hash_value: int):
        self.vector |= hash_value

    def contain(self, hash_value: int) -> False:
        return (self.vector & hash_value) == hash_value


