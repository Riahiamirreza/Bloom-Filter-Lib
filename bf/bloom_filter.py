from bf.hasher import Hasher
from bf.bit_vector import BitVector


class BloomFilter:

    def __init__(self, bit_vector_size: int = 1024):
        self.bit_vector_size = bit_vector_size
        self.hasher = Hasher(size=self.bit_vector_size)
        self.bit_vector =BitVector(size=self.bit_vector_size)

    def insert(self, item: bytes) -> None:
        hash_value: int = self.hasher.hash(item)
        self.bit_vector.add(hash_value)
    
    def contain(self, item: bytes) -> bool:
        hash_value: int = self.hasher.hash(item)
        return self.bit_vector.contain(hash_value) is None
