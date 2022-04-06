##Program to say things about Pushkin
##entering in veriables, adding them to a list, then displaying the list

Pushkin=[]
count=0

print 'What do you think about the cat?'

while count !=5:
    thought=raw_input()
    Pushkin.append(thought)
    count += 1  


for adjective in Pushkin:
        print 'Pushkin is a ' + adjective + ' cat.'

raw_input()
    

