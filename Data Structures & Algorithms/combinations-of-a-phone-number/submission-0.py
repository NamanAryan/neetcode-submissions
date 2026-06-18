class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        
        def backtrack(i, curChar):
            if len(curChar) == len(digits):
                res.append(curChar)
                return

            for c in digitToChar[digits[i]]:
                curChar += c
                backtrack(i + 1, curChar)
                curChar = curChar[:-1]

        if digits:
            backtrack(0, "")
        return res