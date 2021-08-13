##System grading the exam.
## Inform the notes the student and check if he approved or not.

x = int(input('Inform first note: '))
y = int(input('Inform second note: '))
print('You need 7 or more points to be approved. ')

if x <= 10 and y <= 10:
    if x + y > 14:
        print('approved with: {}'.format((x+y)/2)+' points.')
    else:
        print('You not approved, because you need 7 points and you have {}.'. format((x+y)/2))
else:
    print('some note is wrong')