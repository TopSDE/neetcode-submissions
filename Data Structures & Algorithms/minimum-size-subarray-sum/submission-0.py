class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums)
        currSum = 0
        l, r, res = 0, 0, float('inf')
        
        while r < N + 1:
            while currSum >= target:
                currSum -= nums[l]
                res = min(res, r - l)
                l += 1

            if r < N:
                currSum += nums[r]
                r += 1

            else:
                break
            
        return res if res != float('inf') else 0