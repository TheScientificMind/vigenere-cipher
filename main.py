# letters in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# encrypts text using the vigenere cipher based on a key
def encrypt(plaintxt, mykey):
    ciphertxt = ""

    for i in range(len(plaintxt)):
        # if the plaintext at the index is a letter, it gets encrypted 
        # otherwise, it gets added as is
        if plaintxt[i].isalpha():
            # shifts the index
            ind = alphabet.index(plaintxt[i]) + alphabet.index(mykey[i])

            # checks if the index is too high
            if ind > len(alphabet) - 1:
                ind -= len(alphabet)

            ciphertxt += alphabet[ind]
        else:
            ciphertxt += plaintxt[i]
            
    return ciphertxt

# decrypts text using the vigenere cipher based on a key
def decrypt(ciphertxt, mykey):
    plaintxt = ""

    for i in range(len(ciphertxt)):
        # if the ciphertext at the index is a letter, it gets decrypted
        # otherwise, it gets added as is
        if ciphertxt[i].isalpha():
            # shifts the index
            ind = alphabet.index(ciphertxt[i]) - alphabet.index(mykey[i])
            
            plaintxt += alphabet[ind]
        else:
            plaintxt += ciphertxt[i]

    return plaintxt

# ensures the code is being run as a script and not imported as a moduke
if __name__ == "__main__":
    try:    
        text = input("Enter the text you would like to translate: ").lower().strip()

        key = input("Please enter a key: ").lower().strip().replace(" ", "")

        # ensures the key is only composed of letters
        if key.isalpha() != True:
            print("Error: your key contained characters not in the alphabet. Please try again.")
            exit()
        
        # if the key is shorter than the text, makes the key as long as the text
        if len(key) < len(text):
            for i in range(len(text) - len(key)):
                key += key[i]
        
        process = input("Would you like to encrypt or decrypt text (e/d): ").lower().strip()

        # determines whether to encrypt or decrypt the text
        if process == "e":
            print(encrypt(text, key))
        elif process == "d":
            print(decrypt(text, key))
        else:
            print("Error: you entered something other than e or d. Please try again.")
            exit()
    except Exception as err:
        print(f"The program encountered the error:\n\n{err}\n\nPlease run the program to try again.")