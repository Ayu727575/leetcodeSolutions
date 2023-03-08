def colored_cell(ind,dp):
    if ind==0:
        return 1
    if dp[ind]!=-1:
        return dp[ind]
    dp[ind] = ind*4 + colored_cell(ind-1,dp)
    return dp[ind]
def tabu(n):
    dp=[0]*n
    dp[0]=1
    for i in range(1,n):
        dp[i] = dp[i-1]+i*4
    return dp[n-1]
n = int(input())
dp = [-1 for i in range(n)]
print(colored_cell(n-1,dp))
print(tabu(n))
print(dp)