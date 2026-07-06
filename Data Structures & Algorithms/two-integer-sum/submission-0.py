class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for k, v in enumerate(nums):
            diff = target - v
            if diff in hash_map:
                return [hash_map[diff], k]

            hash_map[v] = k