# Decode messages encrypted with a key word cipher
#Read in data from file 'cipherkey.txt'

plain_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
cipher_alphabet = [""] * 26

index = 0

key = input("Please enter cipher key: ")
key = key.upper()
for letter in key:
    cipher_alphabet[index] = letter
    index += 1
    #print(cipher_alphabet)

for letter in plain_alphabet:
    if letter not in cipher_alphabet:
        cipher_alphabet[index] = letter
        index += 1
        #print(cipher_alphabet)

print("Plain:", plain_alphabet)
print("Cipher:", cipher_alphabet)

# End of 'for line in f' loop  
# Choose whether to code or decode
operation = input("Would you like to code or decode? ")
if operation == "code":
    # Ask for plain text to code
    cipher_text = ""
    plain_text = input("Please enter plain text: ")
    plain_input = plain_text.split()
    for word in plain_input:
        for letter in word:
            for alphabet in range (0, 26):
                if letter.upper() == plain_alphabet[alphabet]:
                    cipher_text += cipher_alphabet[alphabet]
        cipher_text += " "
    print(cipher_text[:-1])
elif operation == "decode":
    #Ask for cipher text to decode
    plain_text = ""
    cipher_phrase = input("Please enter ciphered message: ")
    ciphered_input = cipher_phrase.split()
    print(ciphered_input)
    for word in ciphered_input:
        for letter in word:
            for alphabet in range (0, 26):
                if letter.upper() == cipher_alphabet[alphabet]:
                    plain_text += plain_alphabet[alphabet]
        plain_text += " "
    print(plain_text)