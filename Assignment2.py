#1. What is concatenation? Explain and give one example in Python. 
# concatenation mean joinning two strings together. 
name = "Husna"
age = 20
print ("My name is " + name + " and I am" +" " + str (age) + " "+ "years old." )

#2. What is the modulus operator (%)? What does it do? Give an example.
# % is remainder, the shows the reamnded value from division. 
print (10 % 3) # output is 1

#3. List at least 5 Python data types and give one example for each. 
country= "Afghanistan" #string
num = 45 #integer
height = 1.70 #float
imaginary_num= 5j #complex num
bool = True #boolean

#4. Write a Python line that shows how to check the data type of a variable. 
print(type(height))

#5. Convert the string "123" into an integer, a float, and a string.
numbers = "123"
print(int(numbers))
print(float(numbers))
print(str(numbers))

#6. Write one example of each numeric type: int, float, and complex. 
num = 45 #integer
height = 1.70 #float
imaginary_num= 5j #complex num

#7. Explain what the bool() function does. Give one example that becomes True and one that becomes False. 
bool(5)    # True
#bool(0)    # False

#8. List three values that evaluate to True in Python and three values that evaluate to False. 
#True values:
1
"Hello"
[1, 2]
#False values:
#0
#"" (empty string)
#[] (empty list)

#9. Explain the difference between / (division) and // (floor division). Write one example. 
10 / 3   # 3.3333 / gives normal division with decimals
10 // 3  # 3 // gives floor division → whole number rounded down

#10. Write a Python comparison operator example and explain what it checks. 
5 > 3