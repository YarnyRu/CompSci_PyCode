answer = input("Would you like to encode or decode a message? ")
if answer.lower() == 'encode':
    plain_text = input("Please enter the message to be encoded: ")
    plain_text = plain_text.lower()
    plain_words = plain_text.split()
    print(plain_words) #test variable
    cipher_text = ""
    letter_count = 0
    for word in plain_words:
        for letter in word:
            letter_count += 1
            shift = letter_count%2
            if shift == 0:
                shift = 2
            #print(f'Shift for letter {letter_count} is {shift}')
            ascii_plain = ord(letter)
            ascii_cipher = ascii_plain + shift
            # Correcting for running out of range
            if ascii_cipher > 122:
                ascii_cipher -= 26
            elif ascii_cipher < 97:
                ascii_cipher += 26
            cipher_text += chr(ascii_cipher)
        cipher_text += " "
    print(cipher_text)
    
elif answer.lower() == 'decode':
    cipher_text = input("Please enter the message to be decoded: ")
    cipher_text = cipher_text.lower()
    cipher_words = cipher_text.split()
    plain_text = ""
    letter_count = 0
    for word in cipher_words:
        for letter in word:
            letter_count += 1
            shift = letter_count%2
            if shift == 0:
                shift = 2
            #print(f'Shift for letter {letter_count} is {shift}')
            ascii_cipher = ord(letter)
            ascii_plain = ascii_cipher - shift
            # Correcting for running out of range
            if ascii_plain > 122:
                ascii_plain -= 26
            elif ascii_plain < 97:
                ascii_plain += 26
            plain_text += chr(ascii_plain)
        plain_text += " "
    print(plain_text)
else:
    print(f'{answer} was not an option')
print("Thank you for using the variable shift cipher program")