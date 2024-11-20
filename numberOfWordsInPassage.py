#text = input("What text would you like me to analyse?")
file = open("RomeoJuliet.txt", "r")
text = file.read()
word = input("Which word would you like counted? ")

word_list = text.split()

#print(word_list)

count = 0

for i in word_list:
    if i == word:
        count += 1
else:
    print("the number of", word, "in the passage is", count )
