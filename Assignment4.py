# Capitalization
# this method will capitaliz the first letter of every word.
text= "hello 2026"
print(text.capitalize())

#Casefold
#This method will lowerate all the letters of a word.
text= "JAVA"
print(text.casefold())

# Central
# move the text to the center 
text= "Welcome"
print(text.center(30)) 

# Count
# This method count the number of time a letter come in a word.
text= "Apple"
print(text.count("p"))

#endcode
# This method change string to byte 
text= "January"
print(text.encode())

#endswith
#This method check whether the word finish with  specific word that we insert in the argument.
text = "february" 
print(text.endswith("y"))

#Expandtabs
#This method specifies number of spaces between words.
text = "World\tGalaxy\tSun"
print(text.expandtabs(20))

#Find
#This mehod find the posiion of the letters.
text ="Kabul City"
print(text.find("K"))

#Format
#This method replace variable name with it's value.
carpet = "Afghan Carpet" 
price = 20000
print("I like this {}, it is price is {} afghani.  ".format(carpet, price))

#Format_map
# This method replace palceholder with a string. 
info = {"Month": "March", "Time": 6}
text = "My class will start on {Month} at {Time}"
print(text.format_map(info))

# Index
# This method show the position of the letters.
text= "Hello World"
print(text.index("o"))

# isalnum
#This method check whether our string is alphanumeric or not
print("Hello123".isalnum())

# isalpha
# check wheather a string is alphabet or not
print("HI5533".isalpha())



