
def lcst_tabulation(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for j in range(m+1):
        dp[0][j] = 0
    ans = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                ans = max(ans, dp[i][j])
            else: dp[i][j] = 0 
    return ans

def lcst_space_optimization(s1,s2):
    n = len(s1)
    m = len(s2)
    prev = [0 for i in range(m + 1)]
    cur = [0 for i in range(m + 1)]
    ans = 0
    for i in range(1,n+1):
        for j in range(1, m+1):
            if s1[i-1]==s2[j-1]:
                cur[j] = 1 + prev[j-1]
                ans = max(ans, cur[j])
            else: cur[j] = 0 
        prev = cur[:]
    return ans
if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print("The length of common subsequence is",lcst_tabulation(s1,s2))
    print("The length of common subsequence is",lcst_space_optimization(s1,s2))