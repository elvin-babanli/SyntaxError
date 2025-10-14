# Module: Functions
# Part 2

#----------------TASK_1---------------#

def list_product(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

numbers = input("Make by commas: ")

number_list = [int(i) for i in numbers.split(",")] # Note for me. (.split) Bir daha bax.
print("Product: ", list_product(number_list))


#----------------TASK_2---------------#

def find_min(list):
    return min(list)



num_1 = int(input("Add 1th numbers: "))
num_2 = int(input("Add 2th numbers: "))
num_3 = int(input("Add 3th numbers: "))
num_4 = int(input("Add 4th numbers: "))

list = [num_1,num_2,num_3,num_4]
find_min(list)
print("Minimum number:", find_min(list))


#----------------TASK_3---------------#

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_in_range(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
    return count

start = int(input("Add first: "))
end = int(input("Add last: "))

result = count_primes_in_range(start, end)

print("How many prime numbers are in range:", result)



#----------------TASK_4---------------#

# I got help from AI

def remove_target(numbers, target):
    removed_count = numbers.count(target) 
    numbers = [num for num in numbers if num != target]
    return removed_count, numbers 

nums = [1, 3, 5, 3, 7, 3, 9]
target_num = 3
removed, new_list = remove_target(nums, target_num)

print("Removed count:", removed)
print("New list:", new_list)


#----------------TASK_5---------------#

def mix_list(list_1, list_2):
    return list_1 + list_2

list_1 = [1,3,5,7]
list_2 = [2,4,6,8]

total = mix_list(list_1, list_2)
print("Mix list ", total)

#----------------TASK_6---------------#

# Write a function that calculates the power of each element from the list of integers. 
# A value for the power is passed as a parameter, the list is also passed as a parameter. 
# The function returns a new list containing the results.

# I couldn't do it :/
# I will try it later.