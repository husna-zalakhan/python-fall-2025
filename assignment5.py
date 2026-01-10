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

