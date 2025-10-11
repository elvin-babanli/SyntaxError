# Module: Exceptions
# Part 1





#----------------TASK_1---------------#

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if age < 0 or age > 130:
        print("Invalid age")
    else:
        print(f"Hello, {name}! Your age is {age}")
except ValueError:
    print("Please add correct info!")



#----------------TASK_2---------------#


# Exception inside here!

def user_welcome(name_2,age_2):
    try:
        age_2 = int(age_2)
        if age_2 < 0 or age_2 > 130:
            print("Invalid age")
        else:
            print(f"Hello, {name_2}! Your age is {age_2}")
    except ValueError:
        print("Invalid input")

name_2 = input("Enter your name: ")
age_2 = input("Enter your age: ")
info = user_welcome(name_2,age_2)
print(info)



# Exception not inside here!

def user_welcome(name_2,age_2):
    if age_2 < 0 or age_2 > 130:
        print("Invalid age")
    else:
        print(f"Hello, {name_2}! Your age is {age_2}")



try:
    name_2 = input("Enter your name: ")
    age_2 = int(input("Enter your age: "))
    info = user_welcome(name_2,age_2)
    print(info)

except ValueError:

    print("Please add correct info!")


#----------------TASK_3---------------#

print("All numbers should be greater than 0!\n")

numbers = []

try:
    while True:
        user_input = input("Enter numbers or press (E) for exit: ")

        if user_input.lower() == 'e':
            break

        number = int(user_input)

        if number <= 0:
            raise ValueError("Please enter number greater than 0!")

        numbers.append(number)

    print("Numbers:", numbers)
    print("Sum of numbers:", sum(numbers))

except ValueError :
    print("Error!")


#----------------TASK_4---------------#

# Exception inside the function!
def num_calc():
    numbers = []
    try:
        while True:
            user_input = input("Enter numbers or press (E) for exit: ")

            if user_input.lower() == 'e':
              break

            number = int(user_input)

            if number <= 0:
                raise ValueError("Please enter number greater than 0!")


            numbers.append(number)

        print("Numbers:", numbers)
        print("Sum of numbers:", sum(numbers))

    except ValueError:
        print("Error!")

num_calc()



# Exception not inside the function!

def num_calc():
    numbers = []
    while True:
        user_input = input("Enter numbers or press (E) for exit: ")

        if user_input.lower() == 'e':
            break

        number = int(user_input)

        if number <= 0:
            raise ValueError("Please enter number greater than 0!")


        numbers.append(number)
    return numbers


try:
    result = num_calc()
    print("Numbers:", result)
    print("Sum of numbers:", sum(result))
except ValueError as ve:
    print("Error!", ve)
except Exception:
    print("Unexpected error occurred!")
