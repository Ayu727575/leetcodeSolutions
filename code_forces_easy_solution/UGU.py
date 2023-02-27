def ugu(s):
    ans=0
    flag=False
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:
            if not flag and s[i]=="0":
                ans+=1
                flag=True
            elif flag:
                ans+=1
    return ans
n = int(input())
for _ in range(n):
    k = int(input())
    s = input()
    print(ugu(s))
# for s in[*open(0)][2::2]:
#     s = s.strip()
#     k = sum(a!=b for a,b in zip(s,s[1:]))
#     print(max(k-1,0) + ('0' in s and s[0] == '1'))