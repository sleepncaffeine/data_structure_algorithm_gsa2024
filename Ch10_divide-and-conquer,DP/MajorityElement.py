# bf
def majority_element(nums):
    for num in nums:
        if nums.count(num):
            len(nums) // 2
            return num


# dc
def majority_element_dc(nums):
    if len(nums) == 1:
        return nums[0]

    mid = len(nums) // 2
    a = majority_element_dc(nums[:mid])
    b = majority_element_dc(nums[mid:])

    if a == b:
        return a

    return [b, a][nums.count(a) > mid]


# pythonic
def majority_element_pythonic(nums):
    return sorted(nums)[len(nums) // 2]


print(majority_element([3, 2, 3]))  # 3
print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # 2

print(majority_element_dc([3, 2, 3]))  # 3
print(majority_element_dc([2, 2, 1, 1, 1, 2, 2]))  # 2

print(majority_element_pythonic([3, 2, 3]))  # 3
print(majority_element_pythonic([2, 2, 1, 1, 1, 2, 2]))  # 2
