def letterCombinations(digits: str):
    res = []
    letter_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno","7":"qprs","8":"tuv","9":"wxyz"}
    def back_track(i,curr_str):
        if len(curr_str)==len(digits):
            res.append(str(curr_str))
            return
        for c in letter_map[digits[i]]:
            back_track(i+1, curr_str+c)
    if digits:
        back_track(0,"")
    return res
if __name__ == "__main__":
    digits = input()
    print(letterCombinations(digits=digits))