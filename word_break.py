# from typing import List
# def wordBreak(s: str, wordDict: List[str]) -> bool:
#         temp = ""
#         flag = False
#         for i in s:
#             temp+=i
#             if temp in wordDict:
#                 print("----",temp)
#                 temp=""
#                 flag=True
#             else:
#                 flag=False
#         return flag
# s = "aaaaaaa"
# word_d = ["aaaa","aaa"]
# ans = wordBreak(s,word_d)
# print(ans)
s = "aaaaa"
s-="aa"
print(s)