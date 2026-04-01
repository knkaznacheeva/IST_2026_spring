import typing as tp
import string
class caesar:
    @staticmethod 
    def encrypt_caesar(plaintext: str, shift):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    table = str.maketrans(lower + upper, lower[shift:] + lower[:shift] + upper[shift:] + upper[:shift])
        return plaintext.translate(table)

    @staticmethod
    def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
        return caesar.encrypt_caesar(chiphertext, -shift)
