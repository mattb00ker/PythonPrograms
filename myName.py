tron = 'cabbage'
def spam(tron):
    print 'Hello, ' + myName
    myName = 'Waffles'
    print 'Your new name is ' + myName
    tron = myName

    return tron

print 'Hi, what\'s your name??'
myName = raw_input()
spam(myName)
print 'Howdy, ' + tron
