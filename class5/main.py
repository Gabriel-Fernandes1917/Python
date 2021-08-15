## list and tuplas
## tupla is "const" the python
list = [1, 3, 5 , 7]
animal_list = ['dog', 'cat', 'elephante']
print(animal_list[1]) ## print only element 1 in array

for x in animal_list:
    print(x)

print(sum(list)) ## 'sum' sum the elements in array
print(max(list)) ## 'max' show the biggest number in the array
print(max(animal_list))## show the lest letter in ABC ordem

if 'cat' in animal_list:
    print('yes exist cat in the list')
else:
    print('not exist cat in the list')

## append('element') add elements in the array

animal_list.append('wolf')

print(animal_list)

## pop remove elements in the array

animal_list.pop(3) ## remove element to position
animal_list.remove('cat')## remove element to name
print(animal_list)


##.sort ordene array

list.sort()
animal_list.sort()

print(list)
print(animal_list)

##.reverse() ordene in reverse form

list.reverse()
print(list)

print(len(animal_list))## show the number the elements have in the array

tupla_animal = tuple(animal_list) ## convert array in tupla
print(type(tupla_animal))
tupla_animal = list(tupla_animal) ## convert tupla in array
print(tupla_animal)
print('end')