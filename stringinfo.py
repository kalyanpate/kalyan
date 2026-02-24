#string 

#Strings : string is an immutable sequence of Unicode characters
# -enclosed, single or double or triple quotes

# print('Single qutes text')
# print("Double Quote string")
# print('''Triple single quote string''')
# print("""Triple double quote """)

Variabale1="Hello World!"

# #accessing Sting USING SQAURE BRACKET
# print(Variabale1[0])
# print(Variabale1[1:5])

# #update string USING RANGE OPERATOR
# Variabale1 =Variabale1[:6] +'Python'
# print(Variabale1)

# # Variabale1=Variabale1.lower()
# print(Variabale1.upper())

#buil in function 
# print(len(Variabale1)) #lenth of string in chracter count
# print(max(Variabale1))    #maximun time character appreared

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

# ## Escape Character :backslash (\)

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

#Methods

# print(Variabale1.lower())
# print(Variabale1.upper())

# #Exercise
# #1 find the nuber of vowels in a given string

# stringvar="find the nuber of vowels in a given string"
# vowels="aeiou"
# count=0
# for x in stringvar:
#     if x.lower() in vowels: count +=1

# print(count)

