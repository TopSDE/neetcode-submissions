class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * (n+2)

        arr1 = [1] * (n+2)
        arr2 = [1] * (n+2)

        for i in range(1, n+1):
            arr1[i] = nums[i-1] * arr1[i-1]
        
        for i in range(n, 0, -1):
            arr2[i] = nums[i-1] * arr2[i+1]

        for i in range(1, n+1):
            res[i] = arr1[i-1] * arr2[i+1]

        return res[1:n+1]