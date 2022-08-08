import secrets
import time

from bf import BloomFilter


def get_false_positive_ratio(
        bit_vector_size: int = 2**25, 
        space: int = 500000, 
        does_not_contain_attempts: int = 500
    ):
    f = BloomFilter(bit_vector_size=bit_vector_size)
    items = [
        secrets.token_bytes(15) for _ in range(space)
    ]

    t1 = time.time()
    [
        f.insert(item) for item in items
    ]
    t2 = time.time()
    print('t2-t1: ', t2 - t1)
    false_positive_count: int = 0

    t3 = time.time()
    for i in (secrets.token_bytes(25) for _ in range(does_not_contain_attempts)):
        if f.contain(i):
            false_positive_count += 1
    t4 = time.time()
    print('t4-t3: ', t4 - t3)

    return false_positive_count


if '__main__' == __name__:
    c = 1
    attempts = 50000
    total = 0
    for _ in range(c):
        total += get_false_positive_ratio(does_not_contain_attempts=attempts)
    
    print(total)
    print(total/(c*attempts))
