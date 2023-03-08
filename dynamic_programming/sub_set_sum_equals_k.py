class Solution:
    def __init__(self) -> None:
        pass
    def solution(self,arr,target):
        def dfs(ind,target):
            if target==0:
                return True
            if ind==0: return arr[ind]==target
            not_take = dfs(ind-1,target)
            take = False
            if arr[ind]<=target: take=dfs(ind-1,target-arr[ind])
            return not_take or take
        return dfs(len(arr)-1,target)
    def solution_memo(self,arr,target):
        def dfs(ind,target,dp):
            if target==0:
                return True
            if ind==0: return arr[ind]==target
            if dp[ind][target] != -1:
                return dp[ind][target]
            not_take = dfs(ind-1,target,dp)
            take = False
            if arr[ind]<=target: take=dfs(ind-1,target-arr[ind],dp)
            dp[ind][target] = not_take or take
            return dp[ind][target]
        dp = [[-1 for i in range(target+1)] for j in range(len(arr))]
        return dfs(len(arr)-1,target,dp)
    def solution_tabu(self,arr,k):
        n = len(arr)
        dp = [[False for j in range(k+1)] for i in range(n)]
    
        for i in range(n):
            dp[i][0] = True
    
        if arr[0] <= k:
            dp[0][arr[0]] = True
    
        for ind in range(1, n):
            for target in range(1, k+1):
                notTaken = dp[ind-1][target]
                taken = False
                if arr[ind] <= target:
                    taken = dp[ind-1][target-arr[ind]]
                dp[ind][target] = notTaken or taken
    
        return dp[n-1][k]
        # dp = [[0 for i in range(target+1)] for j in range(len(arr))]
        # for i in range(len(arr)): dp[i][0] = True
        # dp[0][arr[0]] = True
        # for i in range(len(arr)):
        #     for j in range(target+1):
        #         not_take = dp[i-1][j]
        #         take =False
        #         if j>=arr[i]: take = dp[i-1][j-arr[i]]
        #         dp[i][j] = take or not_take
        # return dp[len(arr)-1][target]
        
    def solution_opti(self,arr,k):
        n = len(arr)
        prev = [False] * (k + 1)
        prev[0] = True
        if arr[0] <= k:
            prev[arr[0]] = True

        for ind in range(1, n):
            cur = [False] * (k + 1)
            cur[0] = True
            for target in range(1, k + 1):
                not_taken = prev[target]
                taken = False
                if arr[ind] <= target:
                    taken = prev[target - arr[ind]]
                cur[target] = not_taken or taken
            prev = cur

        return prev[k]

if __name__ == "__main__":
    target = int(input())
    arr = list(map(int, input().strip().split()))
    obj = Solution()
    ans = obj.solution(arr, target)
    ans1 = obj.solution_memo(arr, target)
    ans2 = obj.solution_tabu(arr, target)
    ans3 = obj.solution_opti(arr,target)
    print(ans)
    print(ans1)
    print(ans2)
    print(ans3)
