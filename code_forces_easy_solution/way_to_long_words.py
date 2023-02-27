def team(nums):
    count=0
    for r in nums:
        if sum(r)>1:
            count+=1
    return count
n = int(input())
arr = [list(map(int, input().strip().split())) for i in range(n) ]
print(team(arr))
# def way_to_long(word):
#     if len(word)>10:
#         return word[0]+str(len(word[1:-1]))+word[-1]
#     return word
# n = int(input())
# for i in range(n):
#     word = input()
#     print(way_to_long(word))