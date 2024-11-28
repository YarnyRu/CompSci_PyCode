# Decode messages encrypted with a key word cipher
#Read in data from file 'cipherkey.txt'

plain_alphabet = [""] * 26
cipher_alphabet = [""] * 26

line_num = 0

with open('cipherkey.txt') as f:
    for line in f:
        line = line.strip()
        letter_pairs = line.split()
        plain_alphabet[line_num] = letter_pairs[0]
        cipher_alphabet[line_num] = letter_pairs[1]
        line_num += 1
print(cipher_alphabet)

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