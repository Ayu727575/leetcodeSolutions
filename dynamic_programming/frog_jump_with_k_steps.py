from typing import List
import sys
class Solution:
    def __init__(self) -> None:
        pass

    # bottom up approach
    def min_energy(self,nums: List[int], dp: List[int], ind:int,k:int) -> int:
        def min_frog_energy(nums,dp,ind,k):
            min_steps = sys.maxsize
            if ind==0: return 0
            if dp[ind] != -1: return dp[ind]
            for j in range(1,k+1):
                if ind-j>=0:
                    jumps = min_frog_energy(nums,dp,ind-j,k)+ abs(nums[ind]-nums[ind-j])
                    min_steps = min(min_steps,jumps)
            dp[ind] = min_steps
            return dp[ind]
        return min_frog_energy(nums,dp,ind,k) 
    # top down approach     
    def min_energy_tabulation(self,nums:List[int], dp: List[int], n:int, k:int )->int:
        dp[0]=0
        for i in range(1,n):
            min_steps = sys.maxsize
            for j in range(1,k+1):
                if i-j>=0:
                    jumps = dp[i-j] + abs(nums[i]-nums[i-j])
                    min_steps = min(min_steps,jumps)
            dp[i]=min_steps
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
    # print(obj.min_energy(arr,dp,n-1,2))
    print(obj.min_energy_tabulation(arr,dp,n,2))
    # print(obj.min_energy_no_dp(arr,n-1))







