
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
    return ans % (10**9 + 7)
n = 4
p = [0,1,2,3]
l = [0,1,1,1]
print(solution(n,p,l))