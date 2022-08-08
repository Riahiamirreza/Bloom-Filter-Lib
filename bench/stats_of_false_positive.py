import secrets


from bf import BloomFilter


def get_false_positive_ratio(
        bit_vector_size: int = 1024, 
        space: int = 50, 
        does_not_contain_attempts: int = 500
    ):
    f = BloomFilter(bit_vector_size=bit_vector_size)
    items = [
        secrets.token_bytes(15) for _ in range(space)
    ]

    [
        f.insert(item) for item in items
    ]

    false_positive_count: int = 0

    for i in (secrets.token_bytes(25) for _ in range(does_not_contain_attempts)):
        if f.contain(i):
            false_positive_count += 1
    
    return false_positive_count


if '__main__' == __name__:
    c = 200
    attempts = 500
    total = 0
    for _ in range(c):
        total += get_false_positive_ratio(does_not_contain_attempts=attempts)
    
    print(total)
    print(total/(c*attempts))
