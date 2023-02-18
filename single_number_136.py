from collections import Counter


nums = [2,2,5,5,6,7,7]

def single_number(nums):
    # map = Counter(nums)
    # for n in nums:
    #     if map[n] == 1:
    #        return n
    res = nums[0]
    for i in range(1,len(nums)):
        res = res^nums[i]
    return res
print(single_number(nums))


