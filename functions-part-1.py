# Module: Functions
# Part 1

#----------------TASK_1---------------#

# Write a function that prints formatted text given below:
# "Don't compare yourself with anyone in this world...
# if you do so, you are insulting yourself."
# Bill Gates

def text_1():
    print("Don't compare yourself with anyone in this world...")
    print("if you do so, you are insulting yourself.")
    print("Bill Gates")


def text_2():
    print("The only limit to our realization of tomorrow is our doubts of today.")
    print("— Franklin D. Roosevelt")

text_1()
print()
text_2()


#----------------TASK_2---------------#

# Write a function that takes two numbers as a parameter and displays all even numbers in between.


def even_numbers():
    for i in range(x, y+1):
        if i % 2 == 0:
            print(i)




print("1. Even numbers between 1 and 100")
x = int(input("Please choose first value: "))
y = int(input("Please choose second value: "))

even_numbers()


#----------------TASK_3---------------#


# Write a function that prints an empty or solid square made out of some symbol.
# The function takes the following as parameters: the length of the side of the square, a symbol, and a boolean 
# variable:

# if it is True, the square is solid;
# if False, the square is empty.


def square(size, symbol, solid):
    if solid == True:
        for i in range(size):
            for j in range(size):
                print(symbol, end=' ')
            print()
    else:
        for i in range(size):
            for j in range(size):
                if i == 0  or i == -1 or j == 0 or j == -1:
                    print(symbol, end=' ')
                else:
                    print(' ', end=' ')

# Something wrond maybe

size = int(input("Add size: "))
symbol = input("Add symbol: ")
solid_2 = input("Solid? (yes/no): ").lower()

solid = True if solid_2 == 'yes' else False

square(size, symbol, solid)




#----------------TASK_4---------------#

# Write a function that returns the smallest of five numbers. 
# Numbers are passed as parameters.

def small_num(a,b,c,d,e):
    return min(a,b,c,d,e)

a = int(input("A) "))
b = int(input("B) "))
c = int(input("C) "))
d = int(input("D) "))
e = int(input("E) "))

result = small_num(a,b,c,d,e)

print("small one ----> ",result)



#----------------TASK_5---------------#

def product_range(start,end):
    if start > end:
        start, end = end , start
    result = 1
    for i in range(start,end+1):
        result *= i
    return result
    
start = int(input("add num: "))
end = int(input("add secind num: "))

final = product_range(start,end)
print("Product: ", final)


#----------------TASK_6---------------#

def example_num(number):
    return len(str(number))

number_a = int(input("Add num: "))

final_a = example_num(number_a)

print("How nuch number there: ", final_a)

#----------------TASK_7---------------#

def palindrome_number(number):
     num_str = str(number)
     return num_str == num_str[::-1]

num_b = int(input("enter: "))
if palindrome_number(num_b):
     print("palindrome")
else:
     print("not palindrome")

