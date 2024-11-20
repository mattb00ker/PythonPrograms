phone_number = input("What is the phone number? ")

all_numbers = phone_number.isnumeric()

if len(phone_number) == 11 and all_numbers == True:
    print("The number conforms to our requirements")
else:
    print("There's an issue with the number")





