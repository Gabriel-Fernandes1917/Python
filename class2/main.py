
## class2
a =int(input('Info the values: ')) ## input in Python and int to converter string for int
b =int(input('Info the 2 value: '))

add = a+b
sub = a - b
mult = a * b
div = a/b
rest = a % b ## rest the one div
print('* : '+ str(mult)) ## The str to converter int for string
print('- : ' +str(sub))
print('/ : '+str(div))
print('+ : '+str(add))

print('add : {}'.format(add)) ## Other form the to converter elements
print(f'Add: {add}. \nSub: {sub}'. format(add=add, sub=sub))

x = 3
y = 2

print(x/y)
print(int(x/y)) ## round float numbers



