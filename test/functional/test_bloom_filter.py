import unittest

from bf import BloomFilter

class TestBloomFilter(unittest.TestCase):

    def test_does_not_contain_empty_01(self):
        f = BloomFilter()
        self.assertIs(f.contain(b'hello'), False)
        self.assertIs(f.contain(b'Ali'), False)
        self.assertIs(f.contain(b'ok'), False)

    def test_does_contain_item_01(self):
        f = BloomFilter()
        f.insert(b'hello')
        self.assertIs(f.contain(b'hello'), True)

    def test_does_contain_item_02(self):
        f = BloomFilter()
        f.insert(b'ali')
        self.assertIs(f.contain(b'ali'), True)

    def test_does_contain_item_03(self):
        f = BloomFilter()
        f.insert(b'salam')
        self.assertIs(f.contain(b'salam'), True)




if __name__ == "__main__":
    unittest.main()