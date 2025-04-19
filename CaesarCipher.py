def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# مثال:
message = "Hello, World!"
shift_amount = 3

encrypted = caesar_encrypt(message, shift_amount)
decrypted = caesar_decrypt(encrypted, shift_amount)

print("Original:", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
