#Set :-
#-----

students = {'santhosh','hari','akash'}
print(type(students))
print(students)

#add method
students.add('dinesh')
print(students)

#update method
students.update(['amal','navani'])
print(students)

#remove method
students.remove('amal')
print(students)

#discard method
students.discard('amal')
print(students)

#pop method
students.pop()
print(students)

#union method
a = {1,2,3}
b = {3,4,5}
print(a.union(b))

#intersection method
print(a.intersection(b))

#difference method
print(a.difference(b))

#symmetric_difference method
print(a.symmetric_difference(b))

#issubset method
a.remove(1)
b.add(2)
print(a.issubset(b))

#issuperset method
print(b.issuperset(a))
print(a.issuperset(b))

#isdisjoint methods
b.remove(2)
b.remove(3)
print(a.isdisjoint(b))

#dictinory:-
#----------

student = {'name':'santhosh', 'age':25, 'city':'salem'}
print(type(student))

#get method
print(student.get('name'))
print(student.get('age'))
print(student.get('city'))

#keys method
print(student.keys())

#value method
print(student.values())

#items method
print(student.items())

#update method
student.update({'phone':7708135530})
print(student.items())

#pop method
student.pop('age')
print(student.items())

#popitem method
print(student.popitem())
print(student.items())

#setdefault method
student.setdefault('name','santhosh')
student.update({'name':'amal'})
print(student.items())
print()
print('************conditional statements*************')
#conditional statements:-
#-----------------------
#if :-
age = 20

if age >= 18:
    print("Eligible to vote")


#if else:-
age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#elif:-
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
