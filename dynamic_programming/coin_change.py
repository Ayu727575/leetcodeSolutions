import sys
class Solution:
    def __init__(self) -> None:
        pass
    def solution(self, arr, amount):
        if len(arr)==1 and arr[0]<amount:
            return -1
        if amount == 0:
            return 0
        def dfs(n,arr, am, dp):
            minn = sys.maxsize
            if am==amount:
                return 1
            if am>amount:
                return 0
            if dp[n]!=-1:
                return dp[n]
            for j in range(n-1,-1,-1):
                min_count = 1+dfs(j-1,arr, am+arr[j],dp)
                minn = min(minn, min_count)
            dp[n] = minn
            return dp[n]
        dp = [-1]*len(arr)
        return dfs(len(arr)-1,arr,0,dp)
arr = list(map(int,input().strip().split()))
amount = int(input())
obj = Solution()
ans = obj.solution(arr,amount)
print(ans)