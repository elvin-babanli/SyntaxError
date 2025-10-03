# Module: Branching Statements
# Part 1


#----------------TASK_1---------------#

# The user types in three numbers. 
# The program prints the sum or product of these numbers based on the user's choice.

num_1 = float(input("Add first number: "))
num_2 = float(input("Add second number: "))
num_3 = float(input("Add third number: "))

choose = input("Selrct one option (Sum/product): ").lower()

if choose == "sum":
    result = num_1 + num_2 + num_3
    print("Your sum is: ", result)

elif choose == "product":
    result_2 = num_1 * num_2 * num_3
    print("Your product is: ", result_2)

else:
    print("Please use normal value!")


#----------------TASK_2---------------#

# Task 2
# The user types in three numbers. 
# Based on the user's choice, the program prints a maximum of three, 
# a minimum of three, or arithmetic mean of three numbers.


number_1 = float(input("Add first number: "))
number_2 = float(input("Add second number: "))
number_3 = float(input("Add third number: "))

option = input("Choose (Max/Min/Mean): ").lower()
if option == "max":
    result = max(number_1, number_2, number_3)
    print("Your max is: ", result)

elif option == "min":
    result = min(number_1, number_2, number_3)
    print("Your min is: ",result)

elif option == "mean":
    result = (number_1 + number_2 + number_3) / 3
    print("Your mean is: ", result)

else:
    print("Invalid option!")




#----------------TASK_3---------------#

# The user types in the number of meters. 
# Based on the user's choice, the program converts meters to miles, inches, or yards.


value = float(input("White your value in meters: "))
option = input("Choose (Miles/Inches/Yards): ").lower()
if option == "miles":
    result = value * 0.000621371
    print("Your value in miles is: ", result)
    
elif option == "inches":
    result = value * 39.3701
    print("Your value in inches is: ", result)

elif option == "yards":
    result = value * 1.09361
    print("Your value in yards is: ", result)

else:
    print("Invalid option!")
