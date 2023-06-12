def ed_tabu(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = i
    for j in range(m+1):
        dp[0][j] = jdef solution(N, P, L):
            # Initialize the tree data structure
            tree = [[] for _ in range(N + 1)]
        
            # Construct the tree
            for i in range(N - 1):
                tree[P[i]].append(i + 2)
                tree[i + 2].append(P[i])
        
            # Initialize the answer
            ans = 0
        
            # Iterate over all the nodes
            for node in range(1, N + 1):
                # Initialize the maximum sum of distances
                max_dist = 0
        
                # Iterate over all the children of the node
                for child in tree[node]:
                    # Initialize the queue
                    q = [[node, 0]]
        
                    # Initialize the visited array
                    visited = [False] * (N + 1)
        
                    # Mark the current node as visited
                    visited[node] = True
        
                    # Iterate over the queue
                    while q:
                        # Pop the current node
                        curr_node, curr_dist = q.pop(0)
        
                        # Iterate over all the children of the current node
                        for child in tree[curr_node]:
                            # Check if the child is visited
                            if not visited[child]:
                                # Check if the child is the required child
                                if child == child:
                                    # Update the maximum distance
         def solution(N, P, L):
             # Initialize the tree data structure
             tree = [[] for _ in range(N + 1)]
         
             # Construct the tree
             for i in range(N - 1):
                 tree[P[i]].append(i + 2)
                 tree[i + 2].append(P[i])
         
             # Initialize the answer
             ans = 0
         
             # Iterate over all the nodes
             for node in range(1, N + 1):
                 # Initialize the maximum sum of distances
                 max_dist = 0
         
                 # Iterate over all the children of the node
                 for child in tree[node]:
                     # Initialize the queue
                     q = [[node, 0]]
         
                     # Initialize the visited array
                     visited = [False] * (N + 1)
         
                     # Mark the current node as visited
                     visited[node] = True
         
                     # Iterate over the queue
                     while q:
                         # Pop the current node
                         curr_node, curr_dist = q.pop(0)
         
                         # Iterate over all the children of the current node
                         for child in tree[curr_node]:
                             # Check if the child is visited
                             if not visited[child]:
                                 # Check if the child is the required child
                                 if child == child:
                                     # Update the maximum distance
                                     max_dist = max(max_dist, curr_dist + L[curr_node - 1])
                                 else:
                                     # Mark the child as visited
                                     visited[child] = True
         
                                     # Push the child in the queue
                                     q.append([child, curr_dist + L[curr_node - 1]])
         
                 # Update the answer
                 ans += max_dist
         
             # Return the answer modulo 10**9 + 7
             return ans % (10**9 + 7)                           max_dist = max(max_dist, curr_dist + L[curr_node - 1])
                                else:
                                    # Mark the child as visited
                                    visited[child] = True
        
                                    # Push the child in the queue
                                    q.append([child, curr_dist + L[curr_node - 1]])
        
                # Update the answer
                ans += max_dist
        
            # Return the answer modulo 10**9 + 7
            return ans % (10**9 + 7)
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