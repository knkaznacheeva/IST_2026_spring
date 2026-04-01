import random
import string
import caesar

class vigenere:
    @staticmethod
    def encrypt_vigenere(plaintext: str, keyword):
       lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        n = len(keyword)
        ciphertext = list(plaintext)
        for i in range(n):
          if keyword[i] in lower:
            shift = lower.find(keyword[i])
          else:
            shift = upper.find(keyword[i])
          ciphertext[i::n] = caesar.encrypt_ceasar(plaintext[i::n], shift)
          ciphertext = "".join(ciphertext)
          return ciphertext


    def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        n = len(keyword)
        ciphertext = list(ciphertext)
        for i in range(n):
            if keyword[i] in lower:
            shift = lower.find(keyword[i])
        else:
            shift = upper.find(keyword[i])
        cipher_text[i::n] = caesar.encrypt_ceasar(ciphertext[i::n], -shift)
        cipher_text = "".join(cipher_text)
        return cipher_text
