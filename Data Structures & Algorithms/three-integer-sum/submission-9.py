class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                twoSum = -(nums[l] + nums[r])
                if nums[i] == twoSum:
                    res.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1

                elif nums[i] > twoSum:
                    r -= 1

                else:
                    l += 1

        return res

                

                