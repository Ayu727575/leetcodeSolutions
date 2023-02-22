class Solution:
    def __init__(self) -> None:
        pass
    def subsequence_sum(self,nums):
        # using plan recursion
        def subsequence_sum_fun(ind,arr):
            if ind == 0:
                return nums[ind]
            if ind<0:
                return 0
            pick = nums[ind]+subsequence_sum_fun(ind-2,nums)
            not_pick = 0 + subsequence_sum_fun(ind-1,nums)
            return max(pick,not_pick)
        return subsequence_sum_fun(len(nums)-1,nums)
    
    def subsequence_sum_dp(self,nums):
        # using memoization
        def subsequence_sum_fun(ind,arr,dp):
            if ind == 0:
                return nums[ind]
            if ind<0:
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            pick = nums[ind]+subsequence_sum_fun(ind-2,nums,dp)
            not_pick = 0 + subsequence_sum_fun(ind-1,nums,dp)
            dp[ind] = max(pick,not_pick)
            return dp[ind]
        dp = [-1 for i in range(len(nums))]
        return subsequence_sum_fun(len(nums)-1,nums,dp)
    
    def subsequence_sum_dp_tabulation(self,nums):
        # using tabulation
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for ind in range(1,len(nums)):
            take=nums[ind]+dp[ind-2] if ind>1 else nums[ind]
            not_take = 0 + dp[ind-1]
            dp[ind] = max(take,not_take)
        return dp[len(nums)-1]
    
    def subsequence_sum_without_extra_space(self,nums):
        # using without extra space
        prev = nums[0]
        prev2 = 0
        for ind in range(1,len(nums)):
            take=nums[ind]+prev2 if ind>1 else nums[ind]
            not_take = 0 + prev
            curr = max(take,not_take)
            prev2 = prev
            prev = curr
        return prev
        
# arr = [2,1,4,9]
arr = list(map(int, input().strip().split()))
obj = Solution()
ans = obj.subsequence_sum(arr)
ans2 = obj.subsequence_sum_dp(arr)
ans3 = obj.subsequence_sum_dp_tabulation(arr)
ans4 = obj.subsequence_sum_without_extra_space(arr)
print(ans)
print(ans2)
print(ans3)
print(ans4)
    