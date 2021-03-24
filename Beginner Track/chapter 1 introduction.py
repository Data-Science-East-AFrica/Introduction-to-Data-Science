
 ###### INTRODUCTION

# print Hello world

print("Hello Python")

# print shapes

print("0---------")
print("  ||||||||")
print("          --}")

# Asterisks with strings
print("Hello Python " * 5)
print("#"*5)





# Variables --> used to store data in memory of a computer

computers = 40
print(computer)

# update 
computers = 50
print(computers) # now 50
houseRating = 4.5 #floating numbers
is_correct = False or True # boolean values
userName = 'Data science' # Strings


# checkpoint:
# create aprogram for a Fuel station for a train station. Assing number of passangers to 30, driver name and if is full or not.
# solution
passangers = 30
driver_name = "Mr John"
is_full = False / True



### Getting User Input

withdrawal_amount = input("Enter amount to wothdraw ")
print("Welcome to Central bank, aproved amount is " + withdrawal_amount)

###challenge
# print a person's name, d.o.b , and favorite food from a user input perspective



## Convertions and Maths operations
#coversion
int() str() bool() float()
num_users = input("Enter number of users between 100")
computers = 100 / int(num_users) 
print("Collect " + str(computers) + " Computers")
# use type() to check the type of user input or variable assigned

### challenge
# write a program to allow a transportation company to convert lagguage to kg from lbs on their web page and cal price
luggage_lbs = input("enter weight: ")
luggage_kg = luaggage_lbs * 0.45
print(luggae_kg)

luggae_kg = int(luggage_lbs) * 0.45
price = luggage_kg * 25
print(price)


# Strings

Lecture = 'Python for developers'

# escaping character
lecture = "Python's backend is Django"
lecture = 'Python\'s developer course here for free. subscribe'
lecture = ' Pthons course for "Develpopers" '
long_string = """ too long string with multiple line 
    get ready not to get bored
    
    hey 
    
    welcome developer """


# Accessing character
#indexing 0-10, n-1
name = " John Doe "
first_name = name[0]
last_char = name[-1] # last character
print(first_name) # first char

# slicing [index:index]
print(name[0:3]) # 
print(name[0:]) # start to end
print(name[:4]) # prints all upto index 4
print(name[:]) # prints all characters
new_name = name[:] # copys contents of the string to the new-string name

### challenge
# using th variable name computer = "MacBook", what is the ouput of the slice [0:-1] ? Write down before running
computer = "MacBook"
print(computer[0:-1])



#### Lesson 6 Formating Strings
# String contatenation
userName = "John"
sirname = "Doe"
print("Mr " + userName + "[" + sirname + "]" + " is an Engineer")

# F String formating
print(f" Mr {userName} [{sirname}] is an Engineer")

# .format of strings
print("Mr {} [{}] is an Engineer").format(userName, sirname)

# {} format of strings
print("Mr {userName} [{sirname}] is an Engineer", userName, sirName)


# String's Method

# cal total char in a string
myProgram = "Junior developer"
print(len(myProgram)) 
print(myProgram.lower()) # to lower
print(myProgram.upper()) # to uppper
print(myProgram.find('J')) # for more than one char, first index is return, -1 mean no char
print(myProgram.replace("Junior","senior"))
print(myProgram.replace('J','P'))

# check if element/char exist in a char
print("Junior" in myProgram) # returns a boolean value , if misspelled returns false.




# Arithmetic Operations

print(5 + 2) # addition
print(5 -2) # subtraction
print( 5 * 2) # multiplication
print(5 / 2 ) # floating value
print(5/2) # returns only whole numbers
print(5%2) # returns remainder
print(5**2) # returns the power of a number

# incrementing values
i = 5
i = i + 5
print(i) # returns 15
i += 5 # returns same value (augumented opertor) shorter way of increamenting/decrementing value
i -+ 5 # decreament

# Oder of operations
print(5+2*5**2) # BODMAS
# adding parenthesis prioritize its operation

# Math Functions

import math
x = 45.987
print(round(x)) 
print(floor(x))
math......


#Conditional statements
# if statements

# if hot:
    cold outside
    wear a jacket
otherwise
    warm outside
    wear a t-shirt
else
    go  swimming

weather_Cold = True

if waether_Cold:
    print("Cold")
else:
   print("Hot")




# example two
is_hot = True
is_cold = False

if is_cold:
    print("Wear your jacket")
elif is_hot:
    print("Go swimming")
else:
    print("Time for a movie, cool weather")


# challenge
# A middle man owns $10 million stock. 
# a business man will deposit 30% if he/she has bank balance wother $500 Million with the rest as installments
# Else if the business man has balance less than $500 , he pays full amount with no installments

person_one_balance = 600
person_two_balance = 230

if person_two_balance>500:
    print("you will pay $10 with installments")
elif person_two_balance<500:
    print(you will pay in full amount)
print("Business complete")


# EXAMPLE 3
# calculate the deposit amount for propety worth $5000 if the deposit rate if 30% for account with enought credit
propertyCash = 500000
has_credit = True

if has_credit:
    print("You are allowed to transact")
    deposit = propertyCash * 0.3
    deposit = (deposit/100)
else:
    print("Load your Account to be allowed to transact")
print("The deposit amount is $ {} ",deposit )


# LOGICAL OPERATORS
# used in situations where we have multiple choices to make a condietion/decision

#AND--> used when both conditions are true
had_good_grades = True
graduate = True

if had_good_grades and graduate:
    print("You have the job")
else:
    print("You are not qualified")


# OR --> Used when one of the conditions are true 

if had_good_grades or graduate:
    print("You are welcome but must work hard")
else:
    print("Go back to school!!!!")


# NOT
# Does the opposite of the given permision

has_loan = True
create_account = True

if has_loan and not create_account:
    print("Account will be created") # no output because create account now has a False value


# Comparison Operators

# Greater than (>)
age = 18
if age>18:
    print("You can travel alone")
else:
    print("Parent must accompany you")

#  >=, <= , ==, != 
age = 20 

if age == 20:
    print("you are youth")
elif age>0 and age<20:
    print("you are still young")
elif age>20 and <=100:
    print("you are a citizen of the nation, pay tax")
else:
    print("Enter appropriate number of your age")

# Challenge one :
# Create a program using comparison operators that will make sure a password entered by a user 
# has at leas 4 character, not more than 8 characters 
# If lenght of password is ok, print "Strong password", less char print("cannot be less than len"), more char
# print("cannot be more than 8 character")


# Challenge two :
# check output and write a program to do as demonstrated
weight = int(input("Enter your Weight: "))
l_or_k = input("K ()kgs or L ()lbs")
if l_or_k.lower() == "k":
    final_weight = weight / 0.45
    print("you are {} kgs".format(final_weight))
elif l_or_k.lower == "l":
    final_weight = weight * 0.45
    print(f"you are {final_weight} lbs")
else:
    print("Enter correct character")

    


# While Loops
# used to execute a task as long as the conditon still remains true
# execute a block multiple times 
x = 10

while x <= 10:
    print(x)
    x = x + 1
print("End of Loop")


# Challenge one 
# print Right angle Triangle with asterisks using for loop

i = 5
while i <= i:
    print("*" * i)
    i += 1
print("Complete")



# challenge 2;
# The Guesing game using compbined lessons taught:
# create a guessing game that allows user input and validates the inout arcording to the specified range:

guess_number = 5
guess_limit = 3
guess_count = 0

while guess_count < guess_limit:

    guess = int(input("Enter your Guess Number ! "))
    guess_count += 1
    if guess == guess_number:
        print("You won!! ")
        break
else:
    print("You lost")






# The Car Game:

# solution
command = ""
while command != "quit":
    command = input("> ").lower()
    if command =="start":
        print("Car started....")
    elif command == "stopped":
        print("car stopped...")
    elif command=="help":
        print("""
        start -> starts the car
        stop -> stops the car
        quit -> exits the game
        """)
    elif command == "quit":
        print("Game over")
        break
    else:
        print("Command not Found! try Again!!")

# solution
# more simplified boolean solution
# 

command = ""
started = False
while command != "quit":
    command = input("> ").lower()
    if command =="start":
        if started:
            print("car is already started..")
            started = True
        else:
            print("Car started....")
    elif command == "stopped":
        if not started:
            print("Car already stopped")
            started = False
        else:
            print("car stopped...")
    elif command=="help":
        print("""
        start -> starts the car
        stop -> stops the car
        quit -> exits the game
        """)
    elif command == "quit":
        print("Game over")
        break
    else:
        print("Command not Found! try Again!!")





# For Loop
# Used to interate through items or collections or any sequence

for item in "Python Course":
    print(item) # prints each character separately

for languages in ["python","Java","java Script","JQuery","PHP"]:
    print(languages)

for x in range(10):
    print(x) # prints number between 0-10 minus 9 (n-1)

for x in range(10,20):
    print(x) # prints from starting to end range

for x in range(1,20, 4):
    print(x) # prints items ranging from 1-20 in multiples of 4


# challenge:
# calculate total number of students in a school with 5 classes with grdaes  1= 30, 2=40,3=60,4=65,5=12:

school = [30,40,60,65,12]
total_students = 0
for grade in school:
    total_students += grade
print(f"Total number of Students: {total_students}")




# Nested Loop
# using for loop, generate a place x,y cordinate
for x in range(5):
    for y in range (4):
        for z in range (3):
            print(f"({x}, {y}, {z})") # prints all cordiantes in "xyz"

challenge, printing letter F with "xxx" usinf For loop
show complete task and let students write Code

# without for loop
numbers  = [5,2,5,2,2]
for x in numbers:
    print('x'*x)
    
# using nested For Loop
numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)
