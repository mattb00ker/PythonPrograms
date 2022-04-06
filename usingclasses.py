from tank import Tank

print 'Please give name'
myTank = Tank(raw_input())

print 'Your tank\'s name is', str(myTank.name)
print 'You have', str(myTank.ammo), 'ammo'
