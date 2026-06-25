# Username must contain only 10 characters.
# No whitespaces is allowed.
# No numbers are allowed.

username = input("Enter your username: ")
if len(username) > 10:
    print ("Username must be under 10 characters")
elif not username.find(" ")== -1:
    print("Whitespaces are not allowed")
elif not username.isalpha():
    print("Numbers are not allowed")
else:
    print("Welcome!",username)

