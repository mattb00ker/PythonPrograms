a=raw_input()
a=int(a)
b=raw_input()
b=int(b)

while b != 0:
    c= a%b
    a=b
    b=c
    print a, b

print a
