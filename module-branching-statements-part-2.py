# Module: Branching Statements
# Part_2

#----------------TASK_1---------------#

# The user types in a number from 1 to 7 that represents a day of the week.
# Print its name. For example, if the number is 1, then you should display "Monday"; if 2, display "Tuesday," etc.

choose_1 = int(input("Add number(1-7): "))

if choose_1 > 7 or choose_1 < 1:
    print("Only 1-7")

else:
    names = {1:"Monday",2:" Tuesday", 3:"Wednesday", 4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
    print(f"Your day is : {names[choose_1]}")




#----------------TASK_2---------------#

# The user types in a number from 1 to 12 that represents a month. Print its name. 
# For example, if the number is 1, display "January"; if 2, display "February," etc.

choose_2 = int(input("Add number(1-12): "))

if choose_2 > 12 or choose_2 < 1:
    print("Only 1-12")

else:
    names = {1:"January",2:"Febuary", 3:"March", 4:"April",5:"May",6:"June",7:"July", 8:"August",9:"September",10:"October",11:"November",12:"December"}
    print(f"Your month is : {names[choose_2]}")



#----------------TASK_3---------------#

# The user types in a number. 
# If the number is greater than 0, print "Your number is positive"; 
# if it is less than zero, print "Your number is negative"; 
# if it is equal to 0, print "Your number is equal to zero."

choose_3 = float(input("Whrite any number here: "))

if choose_3 == 0:
    print("Your number is zero")

elif choose_3 > 0:
    print("Your number is positive")

elif choose_3 < 0:
    print("Your number is negative")



#----------------TASK_4---------------#

# The user types in two numbers.
# Determine if these numbers are equal. 
# If they are not, print them in ascending order.

choose_4 = float(input("First number: "))
choose2_4 = float(input("Seccond number: "))

if choose_4 == choose2_4:
    print("Your numbers are equal")

else:
    print(sorted([choose_4, choose2_4]))

