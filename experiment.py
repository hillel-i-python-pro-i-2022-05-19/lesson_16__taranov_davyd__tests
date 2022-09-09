def cipher_decrypt_lower(cipher_text, key):
    decrypted = ""
    for symbol in cipher_text:
        if symbol.islower():
            symbol_index = ord(symbol) - ord("a")
            symbol_og_pos = (symbol_index - key) % 26 + ord("a")
            symbol_og = chr(symbol_og_pos)
            decrypted += symbol_og
        elif symbol.isupper():
            symbol_index = ord(symbol) - ord("A")
            symbol_og_pos = (symbol_index - key) % 26 + ord("A")
            symbol_og = chr(symbol_og_pos)
            decrypted += symbol_og
        elif symbol.isdigit():
            symbol_index = ord(symbol) - ord("0")
            symbol_og_pos = (symbol_index - key) % 10 + ord("0")
            symbol_og = chr(symbol_og_pos)
            decrypted += symbol_og
        else:
            decrypted += symbol
    return decrypted


cryptic_text = "Hello, Word 0 1 2 3 4 5 6 7 8 9 0"
i = 15
i2 = -15

plain_text = cipher_decrypt_lower(cryptic_text, i)
plain_text2 = cipher_decrypt_lower(plain_text, i2)

print(f"For key {i}, decrypted text: {plain_text}")
print(f"For key {i2}, decrypted text: {plain_text2}")
