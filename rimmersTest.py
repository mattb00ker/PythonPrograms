file = open("rimmer.txt", "a")

for i in range(400):
    text = "i am a fish."
    file.write(text + "\n")
else:
    file.close()