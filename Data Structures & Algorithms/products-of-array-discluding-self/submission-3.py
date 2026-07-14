class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * (n+2)

        for i in range(1, n+1):
            res[i] = nums[i-1] * res[i-1]

        prefix = 1
        for i in range(n, 0, -1):
            res[i] = res[i-1] * prefix
            prefix *= nums[i-1]

        return res[1:n+1]