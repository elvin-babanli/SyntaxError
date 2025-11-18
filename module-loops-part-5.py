#----------------TASK_1---------------#

# The user types in two numbers. 
# Find the sum of all even, odd numbers and 
# multiples of 9 in the specified range, as well as arithmetic mean of each group.


start  = int(input("First num: "))
end = int(input("Second num: "))

count_1 = 0
sum_1 = 0

print("Even numbers: ")
for i in range(start, end +1):
    if i % 2 == 0:
        count_1 += 1
        sum_1 += i
        print(i)

    
if count_1 != 0:
    total_1 = sum_1 / count_1

print("Count: ",count_1)
print("Sum: ", sum_1)
print("Total: ",total_1)

#----------------------------
count_2 = 0
sum_2 = 0
print("Odd numbers: ")
for i in range(start, end +1):
    if i % 2 != 0:
        count_2 += 1
        sum_2 += i
        print(i)

    
if count_2 != 0:
    total_2 = sum_2 / count_2

print("Count: ",count_2)
print("Sum: ", sum_2)
print("Total: ",total_2)

#-----------------------------
count_3 = 0
sum_3 = 0
print("Only 9: ")
for i in range(start, end +1):
    if i % 9 == 0:
        count_3 += 1
        sum_3 += i
        print(i)
        
if count_3 != 0:
    total_3 = sum_3 / count_3

print("Count: ",count_3)
print("Sum: ", sum_3)
print("Total: ",total_3)





#----------------TASK_2---------------#

# The user types in the length of a line and a symbol to fill the line. 
# Print a vertical line made out of the typed in symbol of the specified length.

#For instance, if the typed in number and symbol are 5 and %, the output will be as follows:

lenght = int(input("Add lenght: "))
symbol = input("Add yuour symbol: ")

for i in range (lenght):
    print(symbol)



#----------------TASK_3---------------#

# The user types in numbers. 
# If the number is greater than 0, print "Your number is positive";
# if it is less than zero, print "Your number is negative"; if it is equal to 0, print "Your number is equal to zero." 
# When the user types in 7, the program stops and prints "Good bye!"

while True:
    choose = float(input("Whrite any number here: "))

    if choose == 7:
        print("Good bye")
        break
    elif choose == 0:
        print("Your number is zero")

    elif choose > 0:
        print("Your number is positive")

    elif choose < 0:
        print("Your number is negative")
    


#----------------TASK_4---------------#


# The user types in numbers. 
# The program must calculate their sum and find the maximum and minimum.
# When the user types in 7, the program stops and prints "Good bye!".

sum = 0
max = None
min = None

while True:
    value = float(input("Add some value: "))

    if value == 7:
        print("Good bye")
        break
    sum += value

    if max is None or  value > max:
        max = value

    if min is None or value < min:
        min = value
    
print("Sum: ",sum)
print("Max: ", max)
print("Min: ", min)



