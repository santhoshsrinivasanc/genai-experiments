#String Handling:-
#---------------
#Create String:-

name = 'Santhosh'
city = 'salem'
message = 'String handling in python'

print('name :',name)
print('city :',city)
print('message :',message)
print()
print('**************Create String*******************')
print()

#String Operations:-
#------------------
#String Intexing:-
#Positive Intexing(string treversing)

print('name 2 intex :',name[2])
print('name 4 intex :',name[4])
print('name 1 intex :',name[1])
print()
print('***************Positive Intexing**************')
print()

#Negative Intexing(back tracking)

print('name -3 intex :',name[-3])
print('name -1 intex :',name[-1])
print('name -2 intex :',name[-2])
print()
print('****************Negative Intexing*************')
print()

#String Slicing:-
#Positive Slicing(positive fetching)

print('0 to 3 intex :',name[0:3])
print('3 to 8 intex :',name[3:8])
print()
print('*****************Positive Slicing*************')
print()

#Negative Slicing(negative fetching)

print('-3 to 8 intex :',name[-3:8])
print('-3 to -8 intex :',name[-8:-3])
print()
print('****************Negative Slicing**************')
print()

#Reverse Slicing(reverse fetching)

print('Reverse name :',name[::-1])

#Left Slicing:-
print('start 3 intex :',name[3:])
print('start 5 intex :',name[5:])
print()
print('*****************Left Slicing*****************')
print()

#Right slicing:-
print('end to 3 intex :',name[:3])
print('end to 6 intex :',name[:6])
print()
print('******************Right slicing***************')
print()

#concatenation:-

print(name+city)
print('10'+'10')
print()
print('******************concatenation***************')
print()

#Repetition:-

print(name*3)
print(city*5)
print()
print('******************Repetition******************')
print()

#String Formating:-
#Manual Formating

print('my name is {0} i am from {1}'.format(name,city))

#Auto Formating
print('my name is %s from %s'%(name,city))

#f-String
print(f'my name is{name} from {city}')
print()
print('*****************String Formating*************')
print()

#String Supporting Functions(String dedicated functions)
#(or)dotted functions

#Find Length
print('name intex length:',len(name))
print('city intex length:',len(city))
print()

#Type Casting
age = 25
language ='    python    '
print('my name is',str(age))

print('print name upper case :',name.upper())
print()

print('print name lower case :',name.lower())
print()

print('print name capitalize :',name.capitalize())
print()

print('print name title case :',name.title())
print()

print('print name swapcase   :',name.swapcase())
print()

print('exact format of language',language)
print()

print('language without white space:',language.strip())
print()

print('remove left side white space:',language.lstrip())
print()

print('remove right side white space:',language.rstrip())
print()

print('I like',language.replace(language,'JAVA'))
print()

text='santhosh-25-salem'
print('split text variable :',text.split('-'))
print()

date=['28','july','2026']
print('/'.join(date))
print()

print(name.find('e'))
print(name.find('n'))

print(name.index('n'))
print()

print('count of s in santhosh',text.count('s'))
print()

print('santhosh start with (a) :',name.startswith('a'))
print()

print('santhosh start with (S) :',name.startswith('S'))
print()

print('santhosh end with (n) :',name.endswith('n'))
print()

print('santhosh end with (h) :',name.endswith('h'))
print()

print('check name is alpha :',name.isalpha())
print()

print('check name is digit :',name.isdigit())
print()

print('check text is alnum :',text.isalnum())
print()

print('print name before,after * :',name.center(20,'*'))
print()

print('check language is space :',language.isspace())
print()

print('print age with 0',str(age).zfill(3))
print()

print('remove the prefix of name :',name.removesuffix('thosh'))

