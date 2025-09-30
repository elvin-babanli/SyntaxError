#-------------------------TASK_1-------------------


def check_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def print_range(start,end):
    for i in range(start,end+1):
        if check_prime(i):
            yield i 

for prime in print_range(10, 30):
    print(prime)

#-------------------------TASK_2--------------------

def is_armstrong(n):
    digits = list(map(int, str(n)))
    power = len(digits)
    total = sum(d**power for d in digits)
    return total == n

def armstrong_range(start, end):
    for number in range(start, end + 1):
        if is_armstrong(number):
            yield number

for a in armstrong_range(100, 999):
    print(a)


#-------------------------TASK_3--------------------

lst = [1,3,5,7,9]

def min_lst(num):
    return min(num)

def max_lst(num):
    return max(num)

def find_min_or_max(list_to_check, function_to_call):
    return function_to_call(list_to_check)


print("Minimum:", find_min_or_max(lst, min_lst))
print("Maximum:", find_min_or_max(lst, max_lst))

#-------------------------TASK_4--------------------

def pizza_base():
    return "Pizza with dough"

def margarita(func):
    def wrapper():
        return func() + " + tomato sauce + cheese"
    return wrapper

def capricosa(func):
    def wrapper():
        return func() + " + tomato sauce + cheese + ham"
    return wrapper

def four_cheeses(func):
    def wrapper():
        return func() + " + tomato sauce + cheese + cheese + cheese + cheese"
    return wrapper

def hawaiian(func):
    def wrapper():
        return func() + " + tomato sauce + cheese + ham + pineapple"
    return wrapper



def mushrooms(func):
    def wrapper():
        return func() + " + mushrooms"
    return wrapper

def pepperoni(func):
    def wrapper():
        return func() + " + pepperoni"
    return wrapper

def olives(func):
    def wrapper():
        return func() + " + olives"
    return wrapper

choice = input("Choose pizza: margarita, capricosa, four_cheeses, hawaiian: (M)(C)(F)(H) ").lower()

if choice == "m":
    pizza = margarita(pizza_base)
elif choice == "c":
    pizza = capricosa(pizza_base)
elif choice == "f":
    pizza = four_cheeses(pizza_base)
elif choice == "h":
    pizza = hawaiian(pizza_base)
else:
    pizza = pizza_base

extra_choice = input("Add extra? mushrooms, pepperoni, olives, none: (M)(P)(O)(N) ").lower()

if extra_choice == "m":
    pizza = mushrooms(pizza)
elif extra_choice == "p":
    pizza = pepperoni(pizza)
elif extra_choice == "o":
    pizza = olives(pizza)


print("\nYour order:")
print(pizza())
