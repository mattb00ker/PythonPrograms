f = open("othello.txt", "r")
text = f.read()
#print(text)
split_text = text.split()
#print(split_text)
count = 0
for i in split_text:
    print(split_text[count])
    if split_text[count] == "Iago":
        split_text[count] = "Darth Vader"

    count = count + 1
else:
    new_text = " ".join(split_text)
f.close()
f = open("othello.txt", "w")
f.write(new_text)
f.close()
