from typing import List
import sys
class Solution:
    def __init__(self) -> None:
        pass

    # bottom up approach
    def min_energy(self,nums: List[int], dp: List[int], ind:int) -> int:
        def min_frog_energy(nums,dp,ind):
            if ind==0: return 0
            if dp[ind] != -1: return dp[ind]
            left = min_frog_energy(nums,dp,ind-1)+ abs(nums[ind]-nums[ind-1])
            right = sys.maxsize
            if ind>1: right = min_frog_energy(nums,dp,ind-2)+ abs(nums[ind]-nums[ind-2]) 
            dp[ind] = min(left,right)
            return dp[ind]     
        return min_frog_energy(nums,dp,ind) 
    # top down approach     
    def min_energy_tabulation(self,nums:List[int], dp: List[int], n:int )->int:
        dp[0]=0
        for i in range(1,n):
            fs = dp[i-1] + abs(nums[i]-nums[i-1])
            ss = sys.maxsize
            if i>1: ss = dp[i-2]+abs(nums[i]-nums[i-2])
            dp[i]=min(fs,ss)
        return dp[n-1] 
    # top down approach     
    def min_energy_no_dp(self,nums:List[int], n:int )->int:
        prev = prev2 = 0
        for i in range(1,n):
            fs = prev + abs(nums[i]-nums[i-1])
            ss = sys.maxsize
            if i>1: ss = prev2+abs(nums[i]-nums[i-2])
            curr=min(fs,ss)
            prev2 = prev
            prev = curr

        return prev
if __name__ == "__main__":
    # arr = [0,1,3,5,6,8,12,17]
    arr = list(map(int, input().strip().split()))
    dp  = [0 for i in range(len(arr))]
    # dp  = [-1 for i in range(len(arr))]
    n = len(arr)
    obj = Solution()
    # print(obj.min_energy(arr,dp,n-1))
    # print(obj.min_energy_tabulation(arr,dp,n-1))
    print(obj.min_energy_no_dp(arr,n-1))



