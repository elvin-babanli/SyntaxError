lst= [1,2,3,4,50,6,7,8,9,10]


choice= int(input("Neçəncini dəyişmək istəyirsən?: "))
print("Your grade: ", lst[choice-1])


new_grade = int(input("Dəyəri daxil edin: "))

lst[choice-1] = (new_grade)
print(lst)