class Solution:
    def splitNum(self, num: int) -> int:
        a = []
        n1=0
        n2=0
        temp = num
        while temp!=0:
            r = temp%10
            a.append(r)
            temp = temp//10
        a.sort()
        for i,n in enumerate(a):
            if i&1==0:
               n1=(n1*10)+n
            else:
                n2=(n2*10)+n
        return n1+n2
# Input: num = 4325
# Output: 59
# Explanation: We can split 4325 so that num1 is 24 and
# num2 is 35, giving a sum of 59. We can prove that 59 is indeed the minimal possible sum.