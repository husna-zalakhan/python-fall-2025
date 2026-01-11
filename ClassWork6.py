# If statement
# temprature = 25

# if temprature < 30:
#     print("hi")

# score=40
# if score==90: #comparison opertor
#     print ("A")

# if score>=80:
#     print("B")

# if score<50:
#     print ("C")
 
#Elif 
score=90

if score>=90:
    print("A")

elif score>=80 and score<90:
    print("B")

elif score<80:
    print("C")
#not
#and
#or
print(True and False) 
print(True or False and False) #true
# python first evaluate and then or
print((True or False) and False) # false
print(False and (True or True)) # python first go with inside the parenthesis
 
# is_raining=True
# print(is_raining)

# pass statement: kayword "pass"
if score>=90:
    pass # wait, don't do anything # pass statement

#shorthand if
# score=81
# if score>=90:print("A+")
# elif score<90:
#     print("B")  #elif need consition, else doesn't need new consition 

# #SHORTHAND IF
# print("A+") if score>=90 else print("B")

# if score>=90:
#     print("a")
# elif 80<score<=90:
#     print("b")
score= 75

grade="A+" if score>=90 else "B" if 80<score<=90 else "C"
print(grade)

# Match Statement
# day=13
# match day: #if day is equal to 2
#     case 1: 
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuseday")
#     case 4:
#         print("wednesday")
#     case _: #default case, if other cases are not being matched , the default cse will run.
#         print("Invalid day")

# | pipe character mean or 
# | = or

day=3
match day:
    case 1|2:
        print("Sunday")

# if gaurd with Match 
# scenario: if number 0,1,2,3,4,5. ....> positive
# if <0 -------> negative

number=0

match number:
    case 0|1|2|3|4|5|6|7|8|9:
        print("positive")

match number:
    case n if n>=0:
        print("positive")
    case _:
        print("Negative") # for any other num print negative
# Syntax error: python recognize it
# logic error: python can't recognize it

# Match - case _ = if - else


#numbers- odd vs even
num=2
#% modulus
match num:
    case n if n%2==0:
        print("Even")
    case _:
        print("odd")
    # case n if n%2!=0:
    #     print("odd")

month = 1
day =4
match day:
    case 1|2|3|4 if month ==1:
        print("hello")




        







