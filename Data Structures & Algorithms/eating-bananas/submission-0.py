class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)
        k = r

        while l <= r:
            hours = 0
            mid = (l + r) // 2
            if mid == 0:
                break
            for i in piles:
                hours += math.ceil(i / mid)
            if hours > h:
                l = mid + 1
            elif hours <= h:
                k = min(k, mid)
                r = mid - 1

        return k