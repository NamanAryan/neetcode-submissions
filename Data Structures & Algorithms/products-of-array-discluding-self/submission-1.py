class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            productL = 1
            productR = 1
            l = 0
            r = len(nums) - 1
            while l != i:
                productL = productL * nums[l]
                l += 1
            while r != i:
                productR = productR * nums[r]
                r -= 1
            
            product = productL * productR
            res.append(product)

        return res

            
