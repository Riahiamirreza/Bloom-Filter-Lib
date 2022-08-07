from hashlib import sha256


class Hasher:
    def __init__(self, size: int):
        self.size = size

    def hash(self, input: bytes) -> int:
        return int(
            sha256(input).hexdigest(), 16
        ) % self.size
