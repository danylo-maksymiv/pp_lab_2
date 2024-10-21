#hexgenerator.py
import random

class HexGenerator:
    hash_symbols = '01234567890abcdef'

    @classmethod
    def generate_hash(cls):
        return '0x'+''.join(random.choice(cls.hash_symbols) for _ in range(64))

    @classmethod
    def generate_address(cls):
        return '0x'+''.join(random.choice(cls.hash_symbols) for _ in range(40))

    @staticmethod
    def generate_bytes(length):
        bytes_ = '01234567890abcdefABCDEF'
        return ''.join(random.choice(bytes_) for _ in range(length))