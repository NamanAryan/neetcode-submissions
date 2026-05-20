class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for i in nums:
            dict1[i] = dict1.get(i, 0) + 1

        return sorted(dict1, key = dict1.get, reverse=True)[:k]

        
        