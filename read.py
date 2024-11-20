f = open("RomeoJuliet.txt")
text = f.read()
sp_text = text.split()
count = 0

for i in sp_text:

    if i == 'and':
        count +=1


print(count)