class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, n):
        def dfs(n):
            if n <= 3:
                return n
            ans = n
            i = 1
            while i*i <= n:
                ans = min(ans, 1 + dfs(n-i*i))
                i += 1
            return ans
        return dfs(n)
    def solve_memo(self, n):
        def dfs(n,dp):
            if n <= 3:
                return n
            if dp[n]!=-1:
                return dp[n]
            ans = n
            i = 1
            while i*i <= n:
                ans = min(ans, 1 + dfs(n-i*i,dp))
                i += 1
            dp[n] = ans
            return dp[n]
        dp = [-1 for i in range(n+1)]
        return dfs(n,dp)
    def solve_tabu(self, n):
        dp = [0]*(n+1)
        dp[0] = 0
        for i in range(1,n+1):
            dp[i] = i
            j = 1
            while j*j <= i:
                sq = j*j
                dp[i] = min(dp[i], 1 + dp[i-sq])
                j += 1
        return dp[n]

        
n = int(input())
obj = Solution()
ans = obj.solve(n)
ans2 = obj.solve_memo(n)
ans3 = obj.solve_tabu(n)
print(ans)
print(ans2)
print(ans3)