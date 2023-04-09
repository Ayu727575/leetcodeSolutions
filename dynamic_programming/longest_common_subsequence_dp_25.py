
def lcsUtil(s1,s2,i,j,dp):
    if i<0 or j<0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if s1[i]==s2[j]:
        dp[i][j] = 1 + lcsUtil(s1,s2,i-1,j-1,dp)
        return dp[i][j] 
    else:
        dp[i][j] = 0 + max(lcsUtil(s1,s2,i-1,j,dp), lcsUtil(s1,s2,i,j-1,dp))
        return dp[i][j]

def lcs(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[-1 for _ in range(n)] for _ in  range(m)]
    return lcsUtil(s1,s2,n-1,m-1,dp)
def lcs_tabulation(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for j in range(m+1):
        dp[0][j] = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1]==s2[j-1]: dp[i][j] = 1 + dp[i-1][j-1]
            else: dp[i][j] = 0 + max(dp[i-1][j],dp[i][j-1])
    len_ = dp[n][m]
    i = n
    j = m
    
    index = len_ - 1
    str_ = ""
    for k in range(1,1+len_):
      str_+="$" #dummy string
    
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            str_ = s1[i - 1] + str_[:-1]
            index -= 1
            i -= 1
            j -= 1
        elif s1[i - 1] > s2[j - 1]:
            i -= 1
        else:
            j -= 1
    
    print("The Longest Common Subsequence is", str_)
    return dp[n][m]
def lcs_space_optimization(s1,s2):
    n = len(s1)
    m = len(s2)
    prev = [0] * (n+1)
    cur = [0] * (m+1)
    for i in range(1,n+1):
        for j in range(1, m+1):
            if s1[i-1]==s2[j-1]: cur[j] = 1 + prev[j-1]
            else: cur[j] = 0 + max(prev[j],cur[j-1])
        prev = cur[:]
    return prev[m]
if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print("The length of common subsequence is",lcs(s1,s2))
    print("The length of common subsequence is",lcs_tabulation(s1,s2))
    print("The length of common subsequence is",lcs_space_optimization(s1,s2))