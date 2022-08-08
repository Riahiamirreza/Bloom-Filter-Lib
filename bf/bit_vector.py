from array import array


class BitVector:
    def __init__(self, size: int):
        # self.vector = array('B', [0] * size)
        # self.vector = bytearray((0,) * size)
        self.vector = 0

    def set_to_one(self, *indices: int):
        for index in indices:
            if not self._is_bit_set(index):
                self._set_bit(index)

    def contain(self, *indices: int) -> bool:
        for index in indices:
            if not self._is_bit_set(index):
                return False
        return True

    def _is_bit_set(self, index: int) -> bool:
        return (self.vector >> index) % 2 != 0

    def _set_bit(self, index: int):
        temp_list = list('{:01024b}'.format(self.vector))
        if temp_list[index] != '1':
            temp_list[index] = '1'
        self.vector = int(''.join(temp_list), 2)