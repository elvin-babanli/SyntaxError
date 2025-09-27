# Module: Branching Statements
# Part 1 

#----------------TASK_1---------------#

# The user types in three numbers. 
# The program prints the sum or product of these numbers based on the user's choice. 

num_1=float(input("Number 1: "))
num_2=float(input("Number 2: "))
num_3=float(input("Number 3: "))

choose=str(input("What you want to do? (Sum / Product)")).lower()

if choose == "sum":
    print(num_1+num_2+num_3)
elif choose =="product":
    print(num_1*num_2*num_3)

else:
    print("wrong")


#----------------TASK_2---------------#

# The user types in three numbers. 
# Based on the user's choice, the program prints a maximum of three, 
# a minimum of three, or arithmetic mean of three numbers.


number_1=float(input("Your first number: "))
number_2=float(input("Your seccond number: "))
number_3=float(input("Your third number: "))

option=str(input("What you want to do? (Max/Min/Mean)")).lower()

# (Note for me )Burada biz LIST kimi də edə bilərik məsələn 
# əgər istifadəçi 5 dəyər əlavə edərsə o zaman bizim sistem çökməməlidir

if option =="max":
    print("Maximum is:", max(number_1, number_2, number_3))

elif option == "min":
    print("Minimum is:", min(number_1,number_2,number_3))

elif option == "mean":
    mean = (number_1 + number_2 + number_3)/3
    print("Mean is:", mean)

else:
    print("Wrong")


# ----------------TASK_3---------------#

# The user types in the number of meters. 
# Based on the user's choice, the program converts meters to miles, inches, or yards.


value = float(input("Add your value (Only Meters): "))
option_2 = input("Choose your option (mile / inch / yard): ").lower()

if option_2 == "mile":
    print(value , " Meters equal to = ",value * 0.000621371," miles" )

elif option_2 == "inch":
    print(value , " Meters equal to = ",value * 39.3701," inches")

elif option_2 == "yard":
    print(value , " Meters equal to = ",value * 1.09361," yards")

else:
    print("Wrong")
