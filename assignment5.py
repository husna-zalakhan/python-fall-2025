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
#outcome: [1, 2, 3, 4]
# [1, 2, 3, 4]

