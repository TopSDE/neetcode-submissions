class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zero_cnt = 0
        prod = 1

        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1
            
        if zero_cnt > 1: return [0] * n

        res = [0] * n
        for i in range(n):
            if nums[i] == 0:
                res[i] = prod

            elif zero_cnt == 0:
                res[i] = prod // nums[i]

        return res