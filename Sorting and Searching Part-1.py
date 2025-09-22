#--------------Task_1------------------------
nums = [4, -2, 3, 1, -5, 6, 2, -1, 0]

result = (sum(nums)) / len(nums)

if result > 0:
    x = (len(nums) *2) // 3
else:
    x = len(nums) //3


part = nums[0:x]
sorted_part = sorted(part)
nums[0:x] = sorted_part

nums[x:] =nums[x:][::-1]

print(nums)

#--------------Task_2------------------------


grades = []

for i in range(0,10):
    grade = int(input("Add your grade: "))
    if grade >= 0 or grade <= 12:
        grades.append(grade)
    else:
        print("Please enter a grade between 0 and 12")


print()
print("------------Choices-------------")
print()
print("1. Show all your grades")
print("2. Take the exam again")
print("3. Check if you can get a scholarship")
print("4. Sort your grades")
print("5. Exit")
print()

choice = input("Enter your choice: ")

while True:
    
    if choice == "1":
        print()
        print("--------------------------------")
        print(grades)
        print("--------------------------------")
        print()

        exit = int(input("Press 0 to exit: "))
        if exit == 0:
            break
    elif choice == "2":
        print()
        # print("Press 0 to exit")
        print("Which subject do you want to retake the exam? (replacing grade)")
        subject = int(input("Enter the subject (1 to 12): "))
        if 1 <= subject <= 10:
            print()
            print("Your current grade for this subject is: ", grades[subject-1])
            print()
            new_grade = int(input("Enter your new grade: "))
            grades[subject-1] = new_grade
            print()
            print("Succesfully removed the old grade")
            print()
            print("--------------------------------")
            print(grades)
            print("--------------------------------")
        else:
            print("Please enter a subject between 1 and 12")
            print()

    elif choice == "3":
        print("--------------------------------")
        print(grades)
        print("--------------------------------")
        print("You need 10.7 agerage grade at least! ")
        if sum(grades) / len(grades) >= 10.7:
            print("Your average is: ",sum(grades) / len(grades))
            print("You can get a scholarship!")
            break
        else:
            print("Your average is: ",sum(grades) / len(grades))
            print("You can't get a scholarship!")
            print()
            break

    elif choice == "4":
        choice = str(input("Ascending or Descending (A/D): ")).lower()
        if choice == "a":
            grades.sort()
            print(grades)
        elif choice == "d":
            grades.sort(reverse=True)
            print(grades)
        else:
            print("Invalid choice")
    
    elif choice == "5":
        print("Goodbye!")
    break
     

#--------------Task_3------------------------

nums = [12,15,17,14,9,5,21,19]
n = len(nums)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            swapped = True
    if not swapped:
        break

print(nums)