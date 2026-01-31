#LOOP

# we have 3 kind of loop
#for loop
#while loop
#do while loop: py doesn't have do while loop

#functions
# function: has input and output
#syntax: def + function name (parameter1, parameter2):
def say_hello():
    print("Hello!") 

say_hello()
say_hello()
say_hello()

#Arguments in functions
def return_explination(number):
    result=number*2
    return result

print(return_explination(1)) #first method
x=return_explination(1) 
print(x) #second method

y=return_explination(3) 
print(y)

z= return_explination(1)+1-2
print(z) 

