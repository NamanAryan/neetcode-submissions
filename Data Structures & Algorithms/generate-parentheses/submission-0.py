class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(sol))
                return
            
            if openN < n:
                sol.append("(")
                backtrack(openN + 1, closeN)
                sol.pop()

            if openN > closeN:
                sol.append(")")
                backtrack(openN, closeN + 1)
                sol.pop()

        backtrack(0, 0)
        return res
        