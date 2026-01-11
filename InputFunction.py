# Input Function
# it is a function wused to take a value from user.

name=input("Enter your name: ")
print("Hello", name, "Welcome" )

# input function always returns string typr data
print(type(name)) #string
age=input("Enter your age: ")
print(type(age)) #string 

# print("your age is", age+20) #error cannot combine str with integer
final_age=int(age)+20
print("your age is", int(age)+20)
print("your age is", final_age)

# if user's age is above 18, they can play the game
# if their age is below 18, they are too young to play the game

age=input("Enter your age: ")
age_to_int=int(age)
if age_to_int>=18:
    print("You can play the game.")
else:
    print("You are too young to play this game.")










