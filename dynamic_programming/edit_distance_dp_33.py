def ed_tabu(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = i
    for j in range(m+1):
        dp[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j] = 0+dp[i-1][j-1]
            else:
                dp[i][j] = 1+min(dp[i-1][j-1],min(dp[i-1][j],dp[i][j-1]))
    
    return dp[n][m]
if __name__ == "__main__":
    s = input()
    s2 = input()
    # print("distinct sunsequence using memoization",solution(s,s2))
    print("distinct sunsequence using tabulation",ed_tabu(s,s2))
    # print("distinct sunsequence using tabulation with space optimization",ds_opt(s,s2))