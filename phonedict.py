def gonna_do():
    print()
    print('find with phone number write (1)')
    print('find by name write (2)')
    print('add user to the dict (3)')
    print("to see the dict (4)")
    print('quit (5)')

    print()

phonedict = {'Amal': 1111111111, 'Mohammed': 2222222222, 'Khadijah': 3333333333, 'Abullah': 4444444444,
             'Rawan': 5555555555, 'Faisal': 6666666666, 'Layla': 7777777777}

def find_name(phone):
    key_list = list(phonedict.keys()) #نحول الدكشنري لليست
    val_list = list(phonedict.values())#نحول القيم لليست
    index = val_list.index(phone)#نحول الرقم لايندكس
    name = key_list[index]#الايندكس يبحث لنا في قيم المفاتيح
    return name


def find_phone(name):
    key_list = list(phonedict.keys()) #نحول الدكشنري لليست
    val_list = list(phonedict.values())#نحول القيم لليست
    index = key_list.index(name)#نحول الاسم لايندكس
    phone = val_list[index]#الايندكس يبحث لنا في قيم الفاليو
    return phone

def add(name,phone):
    list(phonedict)#نحول الدكشنري للبست
    phonedict[name] = phone#نضيف المفتاح و القيمة (الرقم)
    print(name,'added to the dict and the number ',phone)
    print()
    print()
    print('the new dict  : ', list(phonedict.keys()))
    print("numbers",list(phonedict.values()))
    print()


def printter():
    print(list(phonedict.keys()))
    print(list(phonedict.values()))




choose = 0

while choose !=5 :#اذا الخيار اصبح يساوي 5  يخرج

    print('welcome home!!')
    gonna_do()
    choose = int(input('Choose : '))

    if choose == 1 :
        coon = 0
        while coon != 2: #لطالمة انه ما جاب قيمة كرر
            try:
                namebynum = int(input('enter the phone number: '))
            except ValueError:
                print('there is something wrong')
                print()
                print('would you like to try again ?')

                print('press anykey to retry and (2) to back home: ')

                coon = input()

                if  coon.isnumeric() :

                    coon = int(coon)


                continue
            if len(str(namebynum)) < 10 :
                print()
                print('this is less then 10 digits')
                continue
            elif len(str(namebynum)) > 10:
                print()
                print('Error : write only 10 digits')
                continue

            if namebynum in phonedict.values():
                print()
                print('the name of the owner is :', find_name(namebynum))

                print('press anykey to retry and (2) to back home: ')

                coon = input()

                if coon.isnumeric():
                    coon = int(coon)
            else:
                break
        else:
            print("erorr!")




    elif choose == 2 :
        coon=0
        while coon != 2 :
            try:
                phonenumbyname = (input('enter a name to get the number: '))
            except :
                continue
            if phonenumbyname in phonedict.keys():
                print('the phone number is (',find_phone(phonenumbyname),')')
                print()
                print('would you like to try again ?')
                print('press anykey to retry and (2) to back home: ')

                coon = input()

                if coon.isnumeric():
                    coon = int(coon)

            elif phonenumbyname not in phonedict.keys():
                print('this name is not in our dict.. ')
                print('press anykey to retry and (2) to back home: ')

                coon = input()

                if coon.isnumeric():
                    coon = int(coon)

    elif choose == 3:
        coon = 0
        while coon != 2:
            try:
               add(input('add his name : '),int(input("his phone number : ")))
            except ValueError:
                print('please enter right number')

                print()

            else: print('press anykey to add again and (2) to back home: ')

            coon = input()

            if  coon.isnumeric() :

                coon = int(coon)

    elif choose == 4:
        coon =0
        while coon != 2:
            try:
                print("if you want to print the names type (U) ")
                print()
                print('if you want to print numbers type (N)')
                print()
                print("for both type (A)")
                choose2 = input('-->')
            except ValueError:

                print('there is something wrong')
                print()
                print('press anykey to retry and (2) to back home: ')

                coon = input()

                if coon.isnumeric():
                    coon = int(coon)

            if choose2.upper() == "U":
                print(list(phonedict.keys()))

                print()

                print('press anykey to retry and (2) to back home: ')

                coon = input()

                if coon.isnumeric():
                    coon = int(coon)

            elif choose2.upper() == "N":
                print(list(phonedict.values()))

                print('press anykey to retry and (2) to back home: ')

                coon = input()

                if coon.isnumeric():
                    coon = int(coon)


            elif choose2.upper() == "A":
                printter()

                print('press anykey to retry and (2) to back home: ')

                coon = input()

                if coon.isnumeric():
                    coon = int(coon)

            else:
                print("error!")
                print()
                print("please type one of this :")
                print()




