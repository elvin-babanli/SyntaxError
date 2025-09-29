# Module: Loops
# Part 4

#----------------TASK_1---------------#


# The user types in two numbers (start and end points of the range).


# Analyze all the numbers in this range as follows: if the number is a multiple of 7, print it.

first = int(input("Add your first number here: "))
second = int(input("Add your second number here: "))

for i in range (first, second + 1):
    if i % 7 == 0:
        print("There are the numbers: ", i)

    


#----------------TASK_2---------------#


# The user types in two numbers (start and end points of the range). 
# Analyze all the numbers in this range. Print the following:

# All numbers in the range;
# All numbers in the range in descending order;
# All numbers that are multiples of 7;
# How many numbers are multiples of 5.

num_1 = int(input("First number: "))
num_2 = int(input("Second number: "))
print("All numbers in the range:")
for i in range (num_1, num_2 +1):
    print(i)

print("All numbers in the range in descending order: ")
for i in range(num_2, num_1 -1, -1): # (Note for me) tərsdən sayın edərkən buna diqqət et. 
    print(i)

print("All numbers that are multiples of 7: ")
for i in range (num_1, num_2 +1):
    if i % 7 ==0:
        print(i)
        
count = 0
print("How many numbers are multiples of 5: ")
for i in range(num_1, num_2 +1):
    if i % 5== 0:
        count += 1
print(count)



#----------------TASK_3---------------#


#The user types in two numbers (start and end points of the range). 
# Analyze all the numbers in this range. 
# The output should be according to the rules specified below.

#If the number is a multiple of 3 (divisible by 3 without remainder), 
# print the word Fizz. 
# If it is a multiple of 5, print Buzz. If it is a multiple of 3 and 5, print Fizz Buzz. 
# If the number is not a multiple of 3 or 5, print the number itself.


start = int(input("First: "))
end = int(input("Last: "))

for number in range(start, end + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

