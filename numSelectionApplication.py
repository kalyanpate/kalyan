#guess the number
import math
chances=10

num=1
secrete_num= 22 #int(math.random())
while num <=10:

    user_num= int(input("Enter number "))
    if user_num == secrete_num:
        print(f"Cogratulations!, {secrete_num} is correct guessed!")
        break
    else:
        if user_num < secrete_num:
            higher_or_lower="higher"
        else:
            higher_or_lower="lower"
        print(f"The number is {higher_or_lower}")

    # print(num)
    num +=1
    chances-=1
    print(f"you have {chances} left")
    
