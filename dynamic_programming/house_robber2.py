from typing import List
class Solution:
    def robHouse(self, nums: List[int])->int:
        prev = nums[0]
        prev2 = 0
        for ind in range(1,len(nums)):
            take=nums[ind]+prev2 if ind>1 else nums[ind]
            not_take = 0 + prev
            curr = max(take,not_take)
            prev2 = prev
            prev = curr
        return prev
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        return max(self.robHouse(nums[1:]),self.robHouse(nums[:-1]))

# arr = [1,2,3,1]
# output = 4
arr = list(map(int, input().strip().split()))
obj = Solution()
ans = obj.rob(arr)
print(ans)