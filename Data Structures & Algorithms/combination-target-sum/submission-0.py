class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, sol, total):
            if total == target:
                res.append(sol.copy())
                return
            if i >= len(candidates) or total > target:
                return

            sol.append(candidates[i])
            dfs(i, sol, total + candidates[i])  
            sol.pop()

            dfs(i + 1, sol, total)

        dfs(0, [], 0)
        return res