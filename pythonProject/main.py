##

print('what you wait calculate ? \n 1 - average\n')
choice = int(input(''))

if choice == 1:
    samples = [int(input('1- sample\n')), int(input('2- sample\n')), int(input('3- sample\n'))]
    print((samples[0]+samples[1]+samples[2])/3)