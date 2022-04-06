def spam(myName):
    print 'Hello, ' + myName
    myName = 'Waffles'
    print 'Your new name is ' + myName
    return myName

myName = 'Albert'
myName = spam(myName)
print 'Howdy, ' + myName
