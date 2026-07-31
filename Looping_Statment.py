#Nested IF:-
age = 18
weight = 40

if age<=18:
    print('age eligible for donate blood')
    if weight<=50:
        print('eligible weight for donate blood')
    else:
         print('not eligible weight for donate blood')
else:
     print('age not eligible for donate blood')
     
print('**********************************')

#looping statment:-
#-----------------
#for loop

for i in range(6):
    print(i)

print('**********************************')
for i in range(1,6):
    print(i)

print('**********************************')
for i in range(1,6,2):
    print(i)
    
print('**********************************')

#even number

for i in range(1,11):
    if i%2==0:
        print(i)
        
print('**********************************')

#while loop:-
num = 1

while (num<=5):
    print(num)
    num += 1
    
print('**********************************')

#Itretion:-
numbers =[10,20,30,40]

for num in numbers:
    print(num)

print('**********************************')

#Nested for loop:-
#----------------
vowels = ['a', 'e', 'i', 'o', 'u']
students = ['santhosh', 'amal', 'hari', 'navani', 'akash']

for i in students:
   for j in vowels:
        if i.startswith(j):
            print(i)
