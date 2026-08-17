class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        N = len(arr)
        prefix = [0] * N
        prefix[0] = arr[0]
        res = 0

        for i in range(1, N):
            prefix[i] = prefix[i - 1] + arr[i]

        if prefix[k - 1] >= k * threshold:
            res += 1

        for i in range(k, N):
            if prefix[i] - prefix[i - k] >= k * threshold:
                res += 1

        return res