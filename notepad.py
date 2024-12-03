phone_number = input("what is your phone number?")
all_numbers = phone_number.isnumeric()

if len(phone_number) == 11 and all_numbers == True and phone_number[0]=="0":
    print("number is valid")
else:
    print("this number is not valid")