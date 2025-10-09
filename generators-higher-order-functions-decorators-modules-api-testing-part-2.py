#----------------------TASK_1--------------------

def fib_range(start, end):
    x, y = 0, 1
    while x <= end:
        if x >= start:
            yield x
        x, y = y, x + y


for num in fib_range(5, 30):
    print(num)

#----------------------TASK_2--------------------

list1 = [1, 4, 2]
list2 = [3, 6, 5, 5]


def sum_lists(l1, l2):
    max_len = max(len(l1), len(l2))
    for i in range(max_len):
        a = l1[i] if i < len(l1) else 0
        b = l2[i] if i < len(l2) else 0
        yield a + b


for val in sum_lists(list1, list2):
    print(val)

#----------------------TASK_3--------------------


nums = [1,2,3,4]

def square(x):
    return x ** 2


def cube(x):
    return x ** 3



def calculate(list_to_work, function_to_call):
    result = []
    for i in list_to_work:
        result.append(function_to_call(i))
    return result


print(calculate(nums, square))
print(calculate(nums, cube))


#----------------------TASK_4--------------------

def agency_a_format(func):
    def wrapper():
        result = func()
        return f"agency_a_format: {result}"
    return wrapper

def agency_b_format(func):
    def wrapper():
        result = func()
        return result.replace("$","£")
    return wrapper

@agency_a_format
@agency_b_format
def report():
    return "Total revenue: $10000"


print(report())
