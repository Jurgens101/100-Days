#ask user for their name
userName = str(input("Enter your name only: "))
userName = userName.strip(' ')
userNameLength = len(userName)

print("Your name is ", userNameLength," characters long")