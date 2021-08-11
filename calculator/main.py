##Calculator

x = float(input('inform the first value '))
op = int(input('Select the option: 1: + \n 2: - \n 3: / \n 4: * \n'))
y = float(input('inform the second value \n'))


if op == 1:
    print('{} + {} = {}'.format(x, y, x+y))
elif op == 2:
    print('{} - {} = {}'.format(x, y, x - y))
elif op == 3:
    print('{} / {} = {}'.format(x, y, x / y))
elif op == 4:
    print('{} * {} = {}'.format(x, y, x * y))
else:
    print('invalid option')


