
def max_sum(arr,m,n):
    cur_sum = 0
    maxx = 0
    for i in range(m):
        cur_sum += arr[i]
    for i in range(m, n):
        cur_sum = cur_sum + (arr[i] - arr[i-m])
        maxx = max(maxx, cur_sum)
    return maxx

if __name__ == "__main__":
    arr = [10, 20, 10, 30, 5]
    m = 3
    n = 5
    result = max_sum(arr, m, n)
    print(result)