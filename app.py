# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")

'''
character_name = "Tom"
character_date_of_birth = 1970
character_age = "50"
is_male = True
print("There was once a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")
character_name = "Mike"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")
'''

'''
phrase = "Giraffe Academy"
print("Giraffe\nAcademy")
print("Giraffe\"Academy")
print(phrase + " is cool")
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("a"))
print(phrase.replace("Giraffe", "Elephant"))
'''

'''
from math import *
# above is called module, gives access to more math functions
print(-2.0987)
print(3 * (4 + 5))
print(10 % 3)
my_num = -5
print(str(my_num) + " is my favorite number")
print(abs(my_num))
print(pow(4, 6))
print(max(4, 6))
print(round(2.5))
# if 0.5 and odd - round up, if 0.5 and even - round down
print(floor(4.7))
print(ceil(4.7))
print(sqrt(36))
'''

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age)

'''
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
# result = int(num1) + int(num2)
# works only for integer numbers, not decimal numbers
result = float(num1) + float(num2)
# also works for decimal numbers
print(result)
'''

'''
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")
print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)
'''

'''
friends = ["Kevin", "Sophie", "Jim", "Oscar", "Toby"]
friends[1] = "Mike"
print(friends[0])
print(friends[-1])
print(friends[2:])
# above it grabs values starting at index 2 and everything that follows
print(friends[1:3])
# above it grabs values from index 1, up to but not including index 3
'''

'''
lucky_numbers = [42, 8, 15, 16, 23, 4]
friends = ["Kevin", "Sophie", "Jim", "Oscar", "Toby"]
# friends.extend(lucky_numbers)
# friends.append("Creed")
# friends.insert(1, "Kelly")
# friends.remove("Jim")
# friends.pop()
# friends.clear()
friends.sort()
# lucky_numbers.reverse()
lucky_numbers.sort()
print(friends)
# print(friends.index("Kevin"))
# print(friends.count("Oscar"))
friends2 = friends.copy()
print(lucky_numbers)
print(friends2)
'''

'''
coordinates = ((4, 5), (6, 7), (80, 34))
# coordinates[1] = 10
# above not supported because a tuple is used
# for lists use square brackets instead of parentheses
print(coordinates[0])
'''

'''
# use keyword def to create functions
def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))
say_hi("Mike", 35)
say_hi("Steve", 70)
# shown above is how to call a function
'''

'''
def cube(num):
    return num*num*num
# return keyword breaks out of function
result = cube(4)
print(result)
'''

'''
is_male = False
is_tall = True
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not tall")
'''

'''
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        # == checks to see if it is equal and != checks to see if it is unequal
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(3,4,5))
'''

'''
num1 = float(input("Enter first number: "))
op = (input("Enter operator: "))
num2 = float(input("Enter second number: "))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")
'''

'''
month_Conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
# use these "{}" brackets for dictionaries
print(month_Conversions["Nov"])
# above statement is similar to below statement
print(month_Conversions.get("Luv", "Not a valid key"))
# "Not a valid key" is printed as default because first parameter "Luv" does not match dictionary words
'''

'''
i = 1
while i <= 10:
    print(i)
    i += 1
print("Done with loop")
'''

'''
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out Of Guesses, You Lose!")
else:
    print("You Win!")
'''

'''
friends = ["Jim", "Sophie", "Kevin"]
len(friends)
for index in range(len(friends)):
    print(friends[index])
for friend in friends:
    print(friend)
for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not First Iteration")
for index in range(10):
    print(index)
# above prints out numbers from 0 to 9
for index in range(3, 10):
    print(index)
# above prints out numbers from 3 to 9
for letter in "Giraffe Academy":
    print(letter)
'''

'''
print(2**3)
# 2 raised to the 3rd power
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(3, 4))
'''

'''
number_grid = [
    [1, 2, 3],  # row 0
    [4, 5, 6],  # row 1
    [7, 8, 9],  # row 2
    [0]         # row 3
# column #
#    0  1  2
]
print(number_grid[1][2])
# row ( - ) and then column ( | )
for row in number_grid:
    for col in row:
        print (col)
# above is nested for loop
'''

'''
# Giraffe Language
# vowels -> g
# dog -> dgg
# cat -> cgt
def translate(phrase):
    translation = ""
    for letter in phrase:
        # if letter.lower() in "aeiou":   same as below statement
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase: ")))
'''

'''
This is a comment
# This is also a comment
print("Comments are fun")
'''

'''
try:
    answer = 10 / 0 # division by zero error
    number = int(input("Enter a number: ")) # invalid input error if non-numbers are inputted
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")
'''

'''
employee_file = open("employees.txt", "r") # second option is the mode in which you want to open the file
print(employee_file.readable()) # check to see if file is readable
# print(employee_file.read())
# print(employee_file.readline()) # reads first line
# print(employee_file.readline()) # reads second line
for employee in employee_file.readlines():
    print(employee)
# print(employee_file.readlines()[2])
# "r" stands for read; don't want to modify, change, only see what is in the file
# "w" stands for write; change the file, write new information, change existing information
# "a" stands for append; cannot modify or change information in file but can add new information to the end
# "r+" stands for read and write
employee_file.close()
'''

'''
# employee_file = open("employees.txt", "a")
# employee_file = open("employees1.txt", "w") # creates a new file
employee_file = open("index.html", "w")
employee_file.write("<p>This is HTML</p>")
# employee_file = open("employees.txt", "w") # "w" overwrites everything in the existing file
# employee_file.write("\nKelly - Customer Service") # \n appends to a new line, type of escape character
employee_file.close()
'''

'''
import useful_tools
print(useful_tools.roll_dice(10))
# pip can be used to download python modules
# external folders in lib -> site-packages
# pip install and pip uninstall
'''

'''
# classes are used because not all information can be be represented using strings, numbers, or booleans
# classes help to store all the information required in a datatype; classes help define own datatype
from Student import Student
student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)
print(student2.gpa)
# for above; first "Student" refers to the Student file & second "Student" refers to the Student class in that file
# object is just an instance of a class
'''

'''
from Question import Question
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
run_test(questions)
'''

'''
from Student import Student
student1 = Student("Oscar", "Accounting", 3.1, False)
student2 = Student("Phyllis", "Business", 3.8, False)
print(student1.on_honor_roll())
'''

'''
from Chef import Chef
from ChineseChef import ChineseChef
myChef = Chef()
myChef.make_salad()
myChineseChef = ChineseChef()
myChineseChef.make_special_dish()
'''

# You can use command prompt on Windows (or Terminal on Mac) as a Python Interpreter
# simply type "python3" into the command prompt and then you can interact with it