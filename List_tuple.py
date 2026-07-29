#Data Types:-
#----------
#Primitive Data Type

age = 25
price = 88.5
number = 5+10j
is_student = True
name = 'santhosh'

print('age :',type(age))
print('price :',type(price))
print('number :',type(number))
print('is_student :',type(is_student))
print('name :',type(name))
print()
print('***************Primitive Data*****************')

#Non Primitive Data Type:-

fruits = ["Apple", "Banana", "Orange"]
bike = ('ymaha', 'ktm', 'pulsur')
numbers = {10, 20, 30}
details = {
    'name':'santhosh',
    'age' :25
    }
print('fruits :',type(fruits))
print('bike :',type(bike))
print('numbers :',type(numbers))
print('details :',type(details))
print()
print('***************Non Primitive******************')

#List:-

student = ['santhosh', 'amal']
print(student)

#append method
student.append('hari')
print(student)

#extend method
student.extend(['navani', 'akash'])
print(student)

#insert method
student.insert(1,'dinesh')
print(student)

#index method
print(student.index('hari'))

#count method
print(student.count('santhosh'))

#sort method
student.sort()
print(student)

#reverce method
student.reverse()
print(student)

#remove method
student.remove('amal')
print(student)

#copy method (shallow copy)
student1 = student.copy()
print(student1)
student1.append('saravanan')
print(student)
print(student1)

#deep copy
student2 = student
student.remove('dinesh')
print(student)
print(student2)

#pop method
student.pop()
print(student)

#clear method
student.clear()
print(student)
print()
print('*******************List***********************')

#tuple:-

#count method
numbers = (10, 20, 30, 20, 40, 20)
print(numbers.count(20))

#index method
print(numbers.index(40))

print('*******************tuple***********************')



