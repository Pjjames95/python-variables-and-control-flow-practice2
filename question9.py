def has_pair_with_sum(nums, target):
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False

# Example
nums = [1, 2, 3, 9, 4]
target_sum = 8
result = has_pair_with_sum(nums, target_sum)
print("Result:", result)