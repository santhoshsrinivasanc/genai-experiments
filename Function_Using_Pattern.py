#Function using pattern program:-
#------------------------------

while True:
    print('-'*40)
    name = input('Enter Name:')
    num = len(name)
    def name_bit():
        print('-'*10,'BACKWARD INCREAMENT','-'*10)
        for i in range(0,num):
            for j in range(0,num):
                if i+j<=num-1:
                    print(name[i],end='')
                else:
                    print('',end='')
            print()

    def name_bdt():
        print('-'*10,'BACKWARD DECREAMENT','-'*10)
        for i in range(0,num):
            for j in range(0,num):
                if i+j>=num-1:
                    print(name[i],end='')
                else:
                    print('',end=' ')
            print()
    def name_fit():
        print('-'*10,'FARWARD INCREAMENT','-'*10)
        for i in range(0,num):
            for j in range(0,num):
                if i<=j:
                    print(name[i],end='')
                else:
                    print('',end=' ')
            print()

    def name_fdt():
        print('-'*10,'FARWARD DECREAMENT','-'*10)
        for i in range(0,num):
            for j in range(0,num):
                if i>=j:
                    print(name[i],end='')
                else:
                    print('',end=' ')
            print()

    def name_diamand():
        print('-'*16,'DIAMAND','-'*16)
        for i in range(0,num):
            for j in range(0,num):
                if i+j>=num-1-num/2 and i+j<=num-1+num/2 and i>=j-num/2 and i<=j+num/2:
                    print(name[i],end=' ')
                else:
                    print(end='  ')

            print()

    while True:
        print('-' * 40)
        print('      PATTERN GENERATOR MENU')
        print('-' * 40)
        print('1. Backward Triangle')
        print('2. Farward Triangle')
        print('3. Diamond')
        print('0. Exit')
        print('-' * 40)
        
        choice = input('Enter your choice:')
        print()
        if choice=='1':
            while True:
                print('-' * 40)
                print('      BACKWARD TRAINGLE')
                print('-' * 40)
                print('1. Backward Increament Triangle')
                print('2. Backward Decreament Triangle')
                print('0. Exit')
                print('-' * 40)
                choice_t = input('Enter your choice:')
                print()
                
                if choice_t == '1':
                    name_bit()
                elif choice_t == '2':
                    name_bdt()
                elif choice_t=='0':
                    break
                else:
                    print('-' * 40)
                    print('Oops! invalid choice. Please try again.')
        elif choice=='2':
            while True:
                print('-' * 40)
                print('      FARWARD TRAINGLE')
                print('-' * 40)
                print('1. Farward Increament Triangle')
                print('2. Farward Decreament Triangle')
                print('0. Exit')
                print('-' * 40)
                choice_t = input('Enter your choice:')
                if choice_t == '1':
                    name_fit()
                elif choice_t=='0' or choice_t== 'zero':
                    break
                elif choice_t == '2':
                    name_fdt()
                else:
                    print('-' * 40)
                    print('Oops! invalid choice. Please try again.')
        elif choice=='3':
            name_diamand()
        elif choice=='0':
            break
        else:
            print('-' * 40)
            print('Oops! invalid choice. Please try again.')




