## This soft organizer names in alphabetical form

names = [' ',' ',' ',' ',' ',' ']

for i in range(6):
    names[i] = input('inform names {} \n'.format(i+1))

names.sort()
##choice form
print('What form you wait see your list ? \n 1- Array \n 2- List \n')
choice = int(input('inform your option \n'))

if choice == 1:
    print('The list names organizer is: \n')
    print(names)
elif choice == 2:
    print('The list names organizer is: \n')
    for i in range(6):
        print('{}-{}'.format(i+1 ,names[i]))
else:
    print('This option not exist')




