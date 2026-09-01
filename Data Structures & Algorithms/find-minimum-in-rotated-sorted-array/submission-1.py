class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        l, r = 0, N - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] < nums[r]:
                r -= 1

            else:
                l += 1

        return nums[l]