## condicionals
## logical operotors

'''a =int(input('fist value: '))
b = int(input('second value: '))
c = int(input('thert value: '))

if a > b and a >c:
    print('the biggest number is {}'.format(a))
elif b > a and b > c: ## 'elif' is else with if
    print('the biggest number is {}'.format(b))
else:
    print('the biggest number is {}'.format(c))
print('end the program')'''

a = int(input('info the one value: '))

rest = a % 2 ## % div with rest
if rest ==0:
    print('The number {}'.format(a)+' is par')
else:
    print('this number not is par')

