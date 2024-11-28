plain_text = input("Please enter word to be ciphered: ")
cipher_text = ""
shift = int(input("What is the cipher shift (from -13 to +13) "))
while shift < -13 or shift > 13:
    shift = int(input("Please enter an integer between -13 and +13 : "))
for letter in plain_text:
    ascii_plain = ord(letter)
    ascii_cipher = ascii_plain + shift
    if ascii_cipher > 122:
        ascii_cipher = 96 + (ascii_cipher - 122)
        print("Revising cipher")
    cipher_text += chr(ascii_cipher)
print(cipher_text)