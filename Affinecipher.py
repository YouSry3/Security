def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise ValueError(f"No modular inverse for a = {a} under mod {m}")

def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            x = ord(char) - base
            encrypted = (a * x + b) % 26
            result += chr(encrypted + base)
        else:
            result += char
    return result

def affine_decrypt(cipher, a, b):
    result = ""
    a_inv = mod_inverse(a, 26)  # لازم نجيب المعكوس الضربي لـ a
    for char in cipher:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            x = ord(char) - base
            decrypted = (a_inv * (x - b)) % 26
            result += chr(decrypted + base)
        else:
            result += char
    return result

# 🔎 مثال:
message = "Affine Cipher"
a = 5
b = 8

encrypted = affine_encrypt(message, a, b)
decrypted = affine_decrypt(encrypted, a, b)

print("Original:", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
