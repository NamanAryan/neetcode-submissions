class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, sol, curSum):
            if curSum == target:
                res.append(sol[:])
                return

            if i == len(candidates) or curSum > target:
                return
            sol.append(candidates[i])
            dfs(i + 1, sol, curSum + candidates[i])
            sol.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, sol, curSum)
        
        dfs(0, [], 0)
        return res
            