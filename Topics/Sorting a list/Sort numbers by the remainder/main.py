nums = [int(num) for num in list(input())]
print(sorted(nums, key=(lambda num: num % 3)))
# write your code here
