#1....vowel counting
#take string input from user and count the number of vowels in the string

'''s=input()
s2=s.lower() #convert string to lowercase
vowels=s2.count('a') + s2.count('e') + s2.count('i') + s2.count('o') + s2.count('u') #counting number of vowels in the string
print(f"Number of vowels:{vowels}")'''


#2.... students' grade calculator
# Take marks input from user and calculate total marks, average marks and grade based on the following criteria:

'''maths=int(input("marks in maths:"))
science=int(input("marks in science:"))
social=int(input("marks in social:"))

marks=maths+science+social
average=marks/3
percentage=(marks/300)*100
grade=""
if percentage>=90 and percentage<=100:
    grade="A"
elif percentage>=80 and percentage<=90:
    grade="B"
elif percentage>=70 and percentage<=80:
    grade="C"
elif percentage>=60 and percentage<=70:
    grade="D"
else:
    grade="F"

print(f"Total marks:{marks} \naverage marks:{average} \ngrade:{grade}")'''

#3....palindrome checker
#take string input from user and check if the string is a palindrome or not

'''p=input("Enter a string:")

reversed_p=p[::-1] #reverse the string
if p==reversed_p:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")'''

#4....find the largest number
# Take three numbers input from the  user and find the largest number among them

'''a=input("Enter three numbers separated by commas:") #take input as a string
x,y,z=a.split(",") #split the input string into three numbers
num1=int(x)
num2=int(y)
num3=int(z)
largest=(0)

if num1>num2:
    if num1>num3:
        largest=num1
    else:
        largest=num3
elif num2>num1:
    if num2>num3:
        largest=num2
    else:
        largest=num3
elif num3>num2:
    if num3>num1:
        largest=num3
    else:
        largest=num1

print(f"largest number = {largest}")'''

#4...leap year checking

'''a=int(input("enter year: "))

year=a

if year%100 == 0 and year%400 !=0:
    year=(" it is not leap year")
elif year%4 == 0:
    year=("it is  leap year")
else:
    year=("not leap year")

print(year)'''

#5...temperature converter
#take temperature input from user and convert it to the desired unit (Celsius, Fahrenheit, Kelvin)

temp=float(input("enter temperature: "))
unit=input("covert to k or f or c: ")

if unit == "f":
    result = ("temperature in Fahrenheit is: ") + str(temp*(9/5)+32)+"f"
elif unit == "k":
    result = ("temperature in Kelvin is: ") + str(temp+273.15)+"k"
elif unit == "c":
    result = ("temperature in Celsius is: ") + str((temp-32)*5/9) +"c"
else:
    print("Invalid unit")

print(result)

print("hello ")
