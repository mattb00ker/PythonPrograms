password = input("Enter your password: ")

while len(password) < 8 or password.isalpha() or password.isdigit():
    print("Password must be at least 8 characters and contain both letters and numbers.")
    password = input("Enter your password: ")
print("Password accepted!")


