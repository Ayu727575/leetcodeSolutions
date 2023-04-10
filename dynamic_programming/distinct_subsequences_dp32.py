def distinct_subsequence_memo(i,j,s1,s2,dp):
    if j<0: return 1
    if i<0: return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if s1[i] == s2[j]:
        dp[i][j] = distinct_subsequence_memo(i-1,j-1,s1,s2,dp)+ distinct_subsequence_memo(i-1,j,s1,s2,dp)
        return dp[i][j]
    dp[i][j] = distinct_subsequence_memo(i-1,j,s1,s2,dp)
    return dp[i][j]

def ds_tabu(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]+ dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][m]

def ds_opt(s1,s2):
    n = len(s1)
    m = len(s2)
    prev = [0 for _ in range(n+1)]
    curr = [0 for _ in range(m+1)]
    prev[0] = curr[0] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1] == s2[j-1]:
                curr[j] = prev[j-1]+ prev[j]
            else:
                curr[j] = prev[j]
        prev = curr[:]
    return prev[m]


def solution(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[-1 for _ in range(m)] for _ in range(n)]
    res = distinct_subsequence_memo(n-1,m-1,s1,s2,dp)
    return res
    
if __name__ == "__main__":
    s = input()
    s2 = input()
    print("distinct sunsequence using memoization",solution(s,s2))
    print("distinct sunsequence using tabulation",ds_tabu(s,s2))
    print("distinct sunsequence using tabulation with space optimization",ds_opt(s,s2))
