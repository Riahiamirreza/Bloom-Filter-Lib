from hashlib import md5, sha256, sha224, sha384


class Hasher:
    def __init__(self, size: int):
        self.size = size

    def hash(self, input: bytes) -> int:
        md5_digest = md5(input).hexdigest()
        
        digest_1 = int.from_bytes(md5_digest.encode(), 'little')
        digest_2 = int.from_bytes(input, 'little')
        digest_3 = int.from_bytes(input + md5_digest.encode(), 'little')

        return (digest_1 * digest_2 * digest_3) % self.size
