class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        for i in range(n):
            if i-1 < 0: res[i] = nums[i]
            else: res[i] = nums[i] * res[i-1]

        prefix = 1
        for i in range(n-1, -1, -1):
            if i-1 < 0:
                res[i] = prefix
            
            else:
                res[i] = res[i-1] * prefix
                prefix *= nums[i]

        return res
