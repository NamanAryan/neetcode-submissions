class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, sol, curSum):
            if curSum == target:
                res.append(sol[:])
                return
            
            if curSum > target or i >= len(candidates):
                return
            
            sol.append(candidates[i])
            dfs(i, sol, curSum + candidates[i]) 
            sol.pop()

            dfs(i + 1, sol, curSum)

        dfs(0, [], 0)
        return res


