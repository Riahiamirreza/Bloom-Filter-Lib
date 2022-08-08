import unittest
import secrets

from bf import BloomFilter


class TestBloomFilter(unittest.TestCase):
    
    def test_does_contain_01(self):
        f = BloomFilter()
        items = [secrets.token_bytes(10) for _ in range(1000)]
        [
            f.insert(item) for item in items
        ]

        for item in items:
            self.assertIs(f.contain(item), True)

    def test_does_contain_02(self):
        f = BloomFilter(bit_vector_size=2**20)
        items = [secrets.token_bytes(10) for _ in range(10000)]
        [
            f.insert(item) for item in items
        ]

        for item in items:
            self.assertIs(f.contain(item), True)

    def test_does_contain_03(self):
        f = BloomFilter(bit_vector_size=2**20)
        items = [secrets.token_bytes(10) for _ in range(50000)]
        [
            f.insert(item) for item in items
        ]

        for item in items:
            self.assertIs(f.contain(item), True)


if __name__ == '__main__':
    unittest.main()
