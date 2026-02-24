# #print('hello , kalyan')
# nme='kalyan'
# age=269

# #print(nme, ' ', age)

# is_adult=True
# #print(is_adult)

# #name= input("enter name ")
# #print(name)

# #dob = input("what is the age of "+ name + '  ')

# #print(name, "is ", dob , "years old")

# #print(name.upper())

# #print(name.replace('s','A'))

# #print(5*2+3-5)


#  #print(range(5+1))

# # i=0

# # while i in range(5+1):
# # 	#print(i)
# # 	i+=1

# # i=5
# # while i >=0:
# # 	print(i * "*")
# # 	i=i-2

# # for x in range(5):
# # 	print(x)



# # print("triangle")

# # space=4
# # star=1

# # while space >=0:
# # 	print(space *" ")	
# # 	while star <= 5:
# # 		print(star * "*")
# # 		star+=1
# # 	space -=1


# # List
# marks=[10,20,30,40,50]

# # marks.append(60)
# # marks.insert(0,0)
# # for s in marks:
# # 		print(s)

# # print(50 in marks)

# # for s in marks:
# #     if s ==30:
# #         break
# #     print(s)

# # print()

# # for s in marks:
# #     if s ==30:
# #         continue
# #     print(s)

# # def sum(a,b):
# #     print(a+b)
    
# # sum(5,9)



 
#==========================================================
# import sys

# file_name="E:\Programming Code\Ptyhon Course\pythonapp\input.txt"
# file_finish="E:\Programming Code\Ptyhon Course\pythonapp\output.txt"

# try:
#     file = open(file_name,"w")
# except IOError:
#     print("there was an error writing to ", file_name)
#     sys.exit()

# print("Enter '", file_finish)
# print(" ' When Finished")

# file_text=file.read()
# file.close()
# print (file_text)

# while file_text != file_finish:
#     file_text = raw_input("Enter text: ")
#     if file_text == file_finish:
#         file.close()
#         break
#     file.write(file_text)
#     file.write("\n")

# file.close()

# file_name=raw_input("enter_filename: ")
# if len(file_name) == 0:
#     print("Next time please enter somthing")
#     sys.exit()
# try:
#     file=open(file_name,"r")
# except IOError:
#     print("there was an error reading file")
#     sys.exit()



# # #]======================================================

# nma=input("entername")
# print(nma)

# print(type(nma))
# # del nma
# print(nma)

# class MyClass:
#     def __init__(self):
#         self.__private_var ="I am strong!"

#     def show_private(self):
#         return self.__private_var
    
# obj =MyClass()

# # print(obj.show_private())
# print(obj._MyClass__private_var)


# class BankAccounts:
#     def __init__(self, account_number, balance):
#         self.__acount_number= account_number
#         self.__balance=balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance +=amount
#         return self.__balance
    
#     def withdraw(self, amount):
#         if 0 <amount <= self.__balance:
#             self.__balance -= amount
#         return self.__balance
    
#     def get_balamce(self):
#         return self.__balance
    
# account=BankAccounts("12345",1000)

# try:
#     account.__balance += 500
# except AttributeError:
#     print("direct access to private variable failed!!")

# print("your balance account is :", account.get_balamce())

# account.deposit(5000)
# print("your balance account is :", account.get_balamce())
# account.withdraw(500)
# print("your balance account is :", account.get_balamce())

#    *
#   ***
#  *****
# *******

# pylisteng=[12,"ffs",10,"jiom",85]
# print(pylisteng[2], type(pylisteng))
# for i in range(1,5,1):
#     print(i)

# #IF ELIF ELSE
# name= input("enter name - :")

# if name=="kalyan":
#     print("correct Name ")
# elif name=="akk":
#     print("slight miss")
# else:
#     print("enter correct word")

# def checkval(n):
#     match n:
#         case 'a': return "A printed"
#         case 'b': return "b printed"
#         case _: return "simple printed"

# print(checkval('a'))

# def printsr(str, age=15):
#     # "This print a passed striin into this function "
#     # print(str)
#     print("your name is {}".format(str))
#     print("your age is {}".format(age))

#     return
# printsr(age=44, str="Kalyan")
# printsr( str="Kalyan")

# function with return value
# def sum(a,b):
#     c=a+b
#     return c
# a=10;b=10
# print(sum(a,b))

# Anonymous Function
# sum = lambda a,b:a+b
# # print(sum(10,50))

# def div(num, den):
#     q=num/den
#     print("num:{} den: {} q:{}".format(num, den, q))

# div(5,2)

#Module creation & calling
# import mymodule
# mymodule.SayHello("Hari")

# import array as ar

# var= "hello world"
# print(var[1:4])
# print(var[5])

# l1=list(var)
# print(l1)

# arrstr=ar.array('u',var)
# arrstr.append('!')
# print(arrstr)
# var2=arrstr.tounicode()
# print(var2)

# print("Hi %s" % var)

# var111="Welcome to {}"
# print(var111.format("school"))

# value1=2500
# value2=4312
# total=f'Total: {value1 + value2}'
# print(total)

#Strings : string is an immutable sequence of Unicode characters
# -enclosed, single or double or triple quotes

# print('Single qutes text')
# print("Double Quote string")
# print('''Triple single quote string''')
# print("""Triple double quote """)

Variabale1="Hello World!"

# #accessing Sting
# print(Variabale1[0])
# print(Variabale1[1:5])

# #update string
# Variabale1 =Variabale1[:6] +'Python'
# print(Variabale1)

# # Variabale1=Variabale1.lower()
# print(Variabale1.upper())

#buil in function 
# print(len(Variabale1))
# print(max(Variabale1))

#slicing :index
# print(Variabale1[10])
# print(Variabale1[-3])
# print(Variabale1[4:9])
# print(Variabale1[-6:-1])

# Modify String
#1 string to List
# list_var=list(Variabale1)
# print(list_var)

# list_var.insert(3,'L')
# print(list_var)

# var2="".join(list_var)
# print(var2)

# #2 Array
# import array as ar
# arr_var=ar.array("u",Variabale1)

# arr_var2=arr_var.tounicode()
# print(arr_var2)

#concatenation : using "+" operator 
# "*" for replicating string

# # String Formatting
# #1 % operator
# name="kalyan"
# print("Welcome home %s!" % name )
# #2 format()

# var_str="Welcome home {}"
# print(var_str.format("Kalyan Pate"))

# #3 f-string
# price1=152
# price2=415
# total_price= f'Total :{price1+price2}'
# print(total_price)

# #4 Sttring Template class

# from string import Template
# str_var="hello kalyan which city you belongs to is $cityname !"
# templateObj=Template(str_var)

# str_var2=templateObj.substitute(cityname="Pune")
# print(str_var2)

## Escape Character :backslash (\)

# normal="Hello\nKalyan"
# print(normal)
# raw=r"Hello\nKalyan"
# print(raw)

# # ignore \
# s = 'This string will not include \
# backslashes or newline characters.'
# print (s)

# # escape backslash
# s=s = 'The \\character is called backslash'
# print (s)

# # escape single quote
# s='Hello \'Python\''
# print (s)

# # escape double quote
# s="Hello \"Python\""
# print (s)

# # escape \b to generate ASCII backspace
# s='Hel\blo'
# print (s)

# # ASCII Bell character
# s='Hello\a'
# print (s)

# # newline
# s='Hello\nPython'
# print (s)

# # Horizontal tab
# s='Hello\tPython'
# print (s)

# # form feed
# s= "hello\fworld"
# print (s)

# # Octal notation
# s="\101"
# print(s)

# # Hexadecimal notation
# s="\x41"
# print (s)


#==============================
###---LIST---------



# country=["India", "shri Lanka", "cuba", "Ireland","Iran", "Poland","Australia", "Iceland"]
# i_count=0
# for n in country:
#     print(n[0])
#     if n[0]=="I":
#         i_count +=1

# print(i_count)


# number gessing game
import random

number=random.randint(1,10)
# print(number)
def guess_game(number):
    chances=5
    chaceleft=0
    for i in range(chances):
        guess_num=int(input("enter a number: "))
        if number == guess_num:
            print("Congratulations ! you gussed correct number")
            break
        elif number > guess_num:
            print("number is higher")
        elif number < guess_num:
            print("number is lower")
        else:
            print("invalid Input")

        chaceleft +=1
        print(f"{chances-chaceleft} chances are left!")

    print("Game over!")

guess_game(number)
