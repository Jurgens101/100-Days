#using caesar cipher to encode and decode a sentence

alphabet = 'abcdefghijklmnopqrstuvwxyz'
userChoice = input("Do you want to encode or decode?:\n").lower()
userSentence = input("Enter a message:\n").lower()
shift = int(input("Enter the shift number:\n"))

def encrypt(sentence, shiftNumber):
    tempSentence = ""
    for letter in sentence:
        if letter in alphabet:
            x = alphabet.index(letter)
            newPosition = x + shiftNumber
            # Handle wrap-around
            if newPosition >= 26:
                newPosition = newPosition - 26
            tempSentence += alphabet[newPosition]
        else:
            tempSentence += letter
    print(f"The encrypted message is: {tempSentence}")
    return tempSentence

def decrypt(sentence, shiftNumber):
    tempSentence = ""
    for letter in sentence:
        if letter in alphabet:
            x = alphabet.index(letter)
            newPosition = x - shiftNumber
            # Handle wrap-around
            if newPosition < 0:
                newPosition = newPosition + 26
            tempSentence += alphabet[newPosition]
        else:
            tempSentence += letter
    print(f"The decrypted message is: {tempSentence}")
    return tempSentence

if userChoice == "encode":
    encrypt(userSentence, shift)
elif userChoice == "decode":
    decrypt(userSentence, shift)
else:
    print("Please enter a choice between 'encrypt' or 'decrypt'")
