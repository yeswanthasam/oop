name="yash"
print(name)

"""string methods are built-in functions that can be used to manipulate strings"""
print(name.upper()) #string method to convert to uppercase
print(name.lower()) #string method to convert to lowercase
print(name.capitalize()) #string method to capitalize first letter
print(name.title()) #string method to capitalize first letter of each word
print(name.strip()) #string method to remove whitespace from both ends
#print(name.lstrip()) #string method to remove whitespace from left end
#print(name.rstrip()) #string method to remove whitespace from right end
print(name.startswith('y')) #string method to check if string starts with a specific character
print(name.endswith('h')) #string method to check if string ends with a specific character 
print(name.find('a')) #string method to find the index of a specific character
print(name.replace('s','S')) #string method to replace a specific character with another character
print(name.split('s')) #string method to split a string into a list of substrings based on a specific character
print(name.join('123')) #string method to join a list of strings into a single string with a specific character in between
print(name.count('s')) #string method to count the number of occurrences of a specific character in a string
print(name.isalpha()) #string method to check if all characters in a string are alphabetic 
print(name.isdigit()) #string method to check if all characters in a string are digits
print(name.isalnum()) #string method to check if all characters in a string are al
print(name.islower()) #string method to check if all characters in a string are lowercase
print(name.isupper()) #string method to check if all characters in a string are uppercase
print(name.isspace()) #string method to check if all characters in a string are whitespace
print(name.isnumeric()) #string method to check if all characters in a string are numeric
print(name.isdecimal()) #string method to check if all characters in a string are decimal characters