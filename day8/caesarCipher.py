#using caesar cipher to encode and decode a sentence

alphabet = 'abcdefghijklmnopqrstuvwxyz'
keepGoing = True

while keepGoing:
    userChoice = input("Do you want to encode or decode?:\n").lower()
    userSentence = input("Enter a message:\n").lower()
    shift = int(input("Enter the shift number:\n"))


    def caesar(sentence, shiftNumber, direction):
        tempSentence = ""
        for letter in sentence:
            if letter in alphabet:
                x = alphabet.index(letter)
                if direction == "encode":
                    newPosition = x + shiftNumber
                else:
                    newPosition = x - shiftNumber
                # Handle wrap-around
                if newPosition >= 26:
                    newPosition = newPosition - 26
                tempSentence += alphabet[newPosition]
            else:
                tempSentence += letter
        print(f"The encrypted message is: {tempSentence}")
        return tempSentence

    caesar(userSentence, shift, userChoice)
    tryAgain = input("Do you want to try again? Yes or No:\n")
    if tryAgain == "yes":
            keepGoing = True
    else:
            print("Goodbye!")
            keepGoing = False

