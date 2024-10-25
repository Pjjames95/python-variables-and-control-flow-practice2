#with a list given,loop should return the sum of the numbers
#fisrt is to define the function and give a declaration
def sum_list(nums):
    sum = 0
    for num in nums :
        sum += num
    return sum

nums = [1,2,3,4,5]
total = sum_list(nums)
print("The total sum is", total)