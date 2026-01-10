#Lists
nums = [10, 20, 30, 40, 50] 
print(nums[1], nums[-1], nums[-3])
#here is the outcome: 20 50 30

#Slicing
colors = ["red", "blue", "green", "black", "white"] 
print(colors[1:4]) 
print(colors[:3]) 
print(colors[::2])
# outcome: 20 50 30
# ['blue', 'green', 'black']
# ['red', 'blue', 'green']
# ['red', 'green', 'white']

#List methods (append / insert / pop) 
items = ["pen", "book"] 
items.append("laptop") 
items.insert(1, "eraser") 
removed = items.pop(2) 
print(items) 
print(removed) 
#output: ['pen', 'eraser', 'laptop']
#book

#Remove vs Pop
fruits = ["apple", "banana", "orange", "banana"]
removed = fruits.pop(1)
print(fruits)
#outcome: ['apple', 'orange', 'banana']

#copy vs reference
a = [1, 2, 3] 
b = a 
b.append(4) 
print(a) 
print(b) 
#outcome: 
# [1, 2, 3, 4]
# [1, 2, 3, 4]

# Tuples
t1 = ("apple") #F
t2 = ("apple",) #T
print(t1)
print(t2)

#Tuple indexing + slicing 
t = ("a", "b", "c", "d", "e") 
print(t[0]) 
print(t[-1]) 
print(t[1:4])
#Output: 
# a
# e
# ('b', 'c', 'd')

t = (1, 2, 3) 
#t[0] = 99 
print(t) #Error

t = ("a", "b", "c")
temp = list(t)     # convert tuple to list
temp[1] = "B"      # change value
t = tuple(temp)    # convert back to tuple
print(t)
#output:
#('a', 'B', 'c')

#Unpacking with *
t = (10, 20, 30, 40, 50) 
a, b, *c = t 
print(a) #first value
print(b) #second value
print(c) #collect the remaining values into a list
#output: 
# 10
# 20
# [30, 40, 50]

#Dictionary

#Keys vs Values
person = {"name": "Mina", "age": 26, "city": "SLC"} 
print(person)
# keys: name, age, city
# values: Mina, 26, SLC

#Access: [] vs get() 
d = {"a": 1} 
print(d["a"]) 
print(d.get("b")) 
#Why is get() useful? Prevent Error when the key may not exist. 
#output: 
# 1
# None

#Update or add 
student = {"name": "Lina", "score": 90} 
student.update({"score": 95, "passed": True}) 
print(student)
#output: {'name': 'Lina', 'score': 95, 'passed': True}

#Duplicate keys 
d = {"x": 1, "x": 2, "x": 3} 
print(d) 
# output: {'x': 3} python keeps the last value

#Copy vs reference  
d1 = {"a": 1, "b": 2} 
d2 = d1 
d2["b"] = 99 
print(d1) 
print(d2) 
# output:
#{'a': 1, 'b': 99}
#{'a': 1, 'b': 99} we updated the value of b to 99

# Sets

#Duplicates + unordered 
s = {"apple", "banana", "apple", "cherry"} 
print(s) 
# Output:
# {'apple', 'banana', 'cherry'} sets only keep unique values, order does not matter

#Membership + looping 
animals = {"dog", "cat", "bird"} 
if "cat" in animals:
    print ("Yes, cat is in the set.")
else:
    print("No, cat is not in the set.")  

#add() vs update() 
 
s = {"a", "b"}
s.add("c")
s.update(["d", "e"]) 
print(s)
# output: {'c', 'e', 'a', 'b', 'd'}

#remove() vs discard()  
s = {"x", "y"} 
#s.remove("z")   # case A does not exist in the set
#s.discard("z")  # case B Error

#Set operations 
A = {1, 2, 3, 4} 
B = {3, 4, 5} 
print(A.union(B)) 
print(A.intersection(B)) 
print(A.difference(B)) 
print(A.symmetric_difference(B)) 
# Output:
# {'d', 'e', 'a', 'c', 'b'}
# {1, 2, 3, 4, 5}
# {3, 4}
# {1, 2}
# {1, 2, 5}


