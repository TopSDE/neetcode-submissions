class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        N = len(arr)
        currSum = 0
        l, res = 0, 0

        for r in range(N):
            if (r - l) >= k:
                if currSum // k >= threshold:
                    res += 1

                currSum -= arr[l]
                l += 1

            currSum += arr[r]

        if currSum // k >= threshold:
            res += 1

        return res