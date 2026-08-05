#Pattern Programs:-
#----------------
print('*******Forward increament triangle**********')

#Forward increament triangle:-
#---------------------------

#Number:-
#------

num = 6

for i in range(1,num):
    for j in range(1,num):
        if i<=j:
            print(i,end=' ')
        else:
            print(end='  ')

    print()
    
print('*********************************************')

num = 6

for i in range(1,num):
    for j in range(1,num):
        if i<=j:
            print(j,end=' ')
        else:
            print(end='  ')

    print()

print('*********************************************')

#Alphabet Upper:-
#--------------
num =6

for i in range(1,num):
    ch = 65
    for j in range(1,num):
        if i<=j:
            print(chr(ch),end=' ')
            
        else:
            print(end='  ')
        ch +=1

    print()

print('*********************************************')

num =6
ch = 65
for i in range(1,num):
    for j in range(1,num):
        if i<=j:
            print(chr(ch),end=' ')
            
        else:
            print(end='  ')
    ch +=1

    print()
    
print('*********************************************')

#Alphabet lower:-
#--------------
num =6

for i in range(1,num):
    ch = 97
    for j in range(1,num):
        if i<=j:
            print(chr(ch),end=' ')
            
        else:
            print(end='  ')
        ch +=1

    print()

print('*********************************************')

num =6
ch = 97
for i in range(1,num):
    for j in range(1,num):
        if i<=j:
            print(chr(ch),end=' ')
            
        else:
            print(end='  ')
    ch +=1

    print()

print('*********************************************')

#Using Star:-
#----------
num = 6

for i in range(1,num):
    for j in range(1,num):
        if i<=j:
            print('*',end=' ')
        else:
            print(end='  ')

    print()

print('*********************************************')

#Using Name:-
#----------
name = 'santhosh'

for i in range(0,len(name)):
    for j in range(0,len(name)):
        if i<=j:
            print(name[j],end=' ')
        else:
            print(end='  ')

    print()
    
print('*********************************************')

name = 'santhosh'

for i in range(0,len(name)):
    for j in range(0,len(name)):
        if i<=j:
            print(name[i],end=' ')
        else:
            print(end='  ')

    print()

print('_____________________________________________')

print('*******Forward decreament triangle**********')

#Forward decreament triangle:-
#---------------------------

#Number:-
#------

num = 6

for i in range(1,num):
    for j in range(1,num):
        if i>=j:
            print(i,end=' ')
        else:
            print(end='  ')

    print()
    
print('*********************************************')

num = 6

for i in range(1,num):
    for j in range(1,num):
        if i>=j:
            print(j,end=' ')
        else:
            print(end='  ')

    print()

print('*********************************************')

#Alphabet Upper:-
#--------------
num =6

for i in range(1,num):
    ch = 65
    for j in range(1,num):
        if i>=j:
            print(chr(ch),end=' ')
            
        else:
            print(end='  ')
        ch +=1

    print()

print('*********************************************')

num =6
ch = 65
for i in range(1,num):
    for j in range(1,num):
        if i>=j:
            print(chr(ch),end=' ')
            
        else:
            print(end='  ')
    ch +=1

    print()
    
print('*********************************************')

#Alphabet lower:-
#--------------
num =6

for i in range(1,num):
    ch = 97
    for j in range(1,num):
        if i>=j:
            print(chr(ch),end=' ')
            
        else:
            print(end='  ')
        ch +=1

    print()

print('*********************************************')

num =6
ch = 97
for i in range(1,num):
    for j in range(1,num):
        if i>=j:
            print(chr(ch),end=' ')
            
        else:
            print(end='  ')
    ch +=1

    print()

print('*********************************************')

#Using Star:-
#----------
num = 6

for i in range(1,num):
    for j in range(1,num):
        if i>=j:
            print('*',end=' ')
        else:
            print(end='  ')

    print()

print('*********************************************')

#Using Name:-
#----------
name = 'santhosh'

for i in range(0,len(name)):
    for j in range(0,len(name)):
        if i>=j:
            print(name[j],end=' ')
        else:
            print(end='  ')

    print()
    
print('*********************************************')

name = 'santhosh'

for i in range(0,len(name)):
    for j in range(0,len(name)):
        if i>=j:
            print(name[i],end=' ')
        else:
            print(end='  ')

    print()

print('_____________________________________________')

print('*******Backward increament triangle**********')

#Backward increament triangle:-
#---------------------------

#Number:-
#------

num = 6

for i in range(1,num):
    for j in range(1,num):
        if i+j<=num:
            print(i,end=' ')
        else:
            print(end='  ')

    print()
    
print('*********************************************')

num = 6

for i in range(1,num):
    for j in range(1,num):
        if i+j<=num:
            print(j,end=' ')
        else:
            print(end='  ')

    print()

print('*********************************************')

#Alphabet Upper:-
#--------------
num =6

for i in range(1,num):
    ch = 65
    for j in range(1,num):
        if i+j<=num:
            print(chr(ch),end=' ')
            
        else:
            print(end='  ')
        ch +=1

    print()

print('*********************************************')

num =6
ch = 65
for i in range(1,num):
    for j in range(1,num):
        if i+j<=num:
            print(chr(ch),end=' ')
            
        else:
            print(end='  ')
    ch +=1

    print()
    
print('*********************************************')

#Alphabet lower:-
#--------------
num =6

for i in range(1,num):
    ch = 97
    for j in range(1,num):
        if i+j<=num:
            print(chr(ch),end=' ')
            
        else:
            print(end='  ')
        ch +=1

    print()

print('*********************************************')

num =6
ch = 97
for i in range(1,num):
    for j in range(1,num):
        if i+j<=num:
            print(chr(ch),end=' ')
            
        else:
            print(end='  ')
    ch +=1

    print()

print('*********************************************')

#Using Star:-
#----------
num = 6

for i in range(1,num):
    for j in range(1,num):
        if i+j<=num:
            print('*',end=' ')
        else:
            print(end='  ')

    print()

print('*********************************************')

#Using Name:-
#----------
name = 'santhosh'

for i in range(0,len(name)):
    for j in range(0,len(name)):
        if i+j<=len(name)-1:
            print(name[j],end=' ')
        else:
            print(end='  ')

    print()
    
print('*********************************************')

name = 'santhosh'

for i in range(0,len(name)):
    for j in range(0,len(name)):
        if i+j<=len(name)-1:
            print(name[i],end=' ')
        else:
            print(end='  ')

    print()

print('_____________________________________________')

print('*******Backward decreament triangle**********')

#Backward decreament triangle:-
#---------------------------

#Number:-
#------

num = 6

for i in range(1,num):
    for j in range(1,num):
        if i+j>=num:
            print(i,end=' ')
        else:
            print(end='  ')

    print()
    
print('*********************************************')

num = 6

for i in range(1,num):
    for j in range(1,num):
        if i+j>=num:
            print(j,end=' ')
        else:
            print(end='  ')

    print()

print('*********************************************')

#Alphabet Upper:-
#--------------
num =6

for i in range(1,num):
    ch = 65
    for j in range(1,num):
        if i+j>=num:
            print(chr(ch),end=' ')
            
        else:
            print(end='  ')
        ch +=1

    print()

print('*********************************************')

num =6
ch = 65
for i in range(1,num):
    for j in range(1,num):
        if i+j>=num:
            print(chr(ch),end=' ')
            
        else:
            print(end='  ')
    ch +=1

    print()
    
print('*********************************************')

#Alphabet lower:-
#--------------
num =6

for i in range(1,num):
    ch = 97
    for j in range(1,num):
        if i+j>=num:
            print(chr(ch),end=' ')
            
        else:
            print(end='  ')
        ch +=1

    print()

print('*********************************************')

num =6
ch = 97
for i in range(1,num):
    for j in range(1,num):
        if i+j>=num:
            print(chr(ch),end=' ')
            
        else:
            print(end='  ')
    ch +=1

    print()

print('*********************************************')

#Using Star:-
#----------
num = 6

for i in range(1,num):
    for j in range(1,num):
        if i+j>=num:
            print('*',end=' ')
        else:
            print(end='  ')

    print()

print('*********************************************')

#Using Name:-
#----------
name = 'santhosh'

for i in range(0,len(name)):
    for j in range(0,len(name)):
        if i+j>=len(name)-1:
            print(name[j],end=' ')
        else:
            print(end='  ')

    print()
    
print('*********************************************')

name = 'santhosh'

for i in range(0,len(name)):
    for j in range(0,len(name)):
        if i+j>=len(name)-1:
            print(name[i],end=' ')
        else:
            print(end='  ')

    print()

print('*******Diamond**********')

#Diamond:-
#-------

#Star:-
#------

num = 9
for i in range(0,num):
    for j in range(0,num):
        if i+j>=num-1-num/2 and i+j<=num-1+num/2 and i>=j-num/2 and i<=j+num/2:
            print('*',end=' ')
        else:
            print(end='  ')

    print()

print('*********************************************')

#number:-
#------

num = 9
n =1
for i in range(0,num):
    for j in range(0,num):
        if i+j>=num-1-num/2 and i+j<=num-1+num/2 and i>=j-num/2 and i<=j+num/2:
            print(n,end=' ')
        else:
            print(end='  ')
    n +=1

    print()

print('*********************************************')

#Alphabet upper:-
#--------------
num = 9
ch = 65
for i in range(0,num):
    for j in range(0,num):
        if i+j>=num-1-num/2 and i+j<=num-1+num/2 and i>=j-num/2 and i<=j+num/2:
            print(chr(ch),end=' ')
        else:
            print(end='  ')
    ch +=1

    print()

print('*********************************************')

#Alphabet lower:-
#---------------

num = 9
ch = 97
for i in range(0,num):
    for j in range(0,num):
        if i+j>=num-1-num/2 and i+j<=num-1+num/2 and i>=j-num/2 and i<=j+num/2:
            print(chr(ch),end=' ')
        else:
            print(end='  ')
    ch +=1

    print()

print('*********************************************')

#Using name:-
#-----------

name = 'santosh'
num =len(name)

for i in range(0,num):
    for j in range(0,num):
        if i+j>=num-1-num/2 and i+j<=num-1+num/2 and i>=j-num/2 and i<=j+num/2:
            print(name[i],end=' ')
        else:
            print(end='  ')

    print()

print('*******pyramid**********')

#Upside Pyramid:-
#---------------

#number:-
#------

num = 9
print()
for i in range(0,num+1):
    n=1
    for j in range(0,num+1):
        if i+j<=num+1 and i<=j:
            print(n,end=' ')
            n+=1
        else:
            print(end='  ')
       
    print()


print('*********************************************')

#Pyramid:-
#-------

#number:-
#------

num = 9

for i in range(0,num+1):
    n=1
    for j in range(0,num+1):
        if i+j>=num+1 and i>=j:
            print(n,end=' ')
            n+=1
        else:
            print(end='  ')
       
    print()
print('*********************************************')

num = 9

print()
for i in range(0,num+1):
    ch=65
    for j in range(0,num+1):
        if i+j<=num+1 and i<=j:
            print(chr(ch),end=' ')
        else:
            print(end='  ')
        ch+=1   
    print()


print('*********************************************')

num = 9

print()
for i in range(0,num+1):
    ch=65
    for j in range(0,num+1):
        if i+j>=num+1 and i>=j:
            print(chr(ch),end=' ')
            ch+=1 
        else:
            print(end='  ')
         
    print()


print('*********************************************')

#Left side Pyramid:-
#-------

#number:-
#------

num = 9
print()
for i in range(0,num+1):
    n=1
    for j in range(0,num+1):
        if i+j<=num-1 and i>=j:
            print(n,end=' ')
            n+=1
        else:
            print(end='  ')
       
    print()

print('*********************************************')

#Right side Pyramid:-
#-------

#number:-
#------

num = 9
print()
for i in range(0,num+1):
    n=1
    for j in range(0,num+1):
        if i+j>=num+1 and i<=j:
            print(n,end=' ')
            n+=1
        else:
            print(end='  ')
       
    print()

    
print('****************Sand clock*******************')

#Sand clock:-
#----------

num = 9
for i in range(0,num):
    n=1
    for j in range(0,num):
        if i+j<=num-1 and i<=j or i+j>=num-1 and i>=j:
            print(n,end=' ')
           
        else:
            print(end='  ')
        n+=1
    print()
print('*********************************************')

#Opposite sand clock:-
#-------------------

num = 9
print()
for i in range(0,num):
    n=1
    for j in range(0,num):
        if i+j<=num-1 and i>=j or i+j>=num-1 and i<=j:
            print(n,end=' ')
           
        else:
            print(end='  ')
        n+=1
    print()


    







