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