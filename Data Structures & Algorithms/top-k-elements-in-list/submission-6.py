class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        hash_map = Counter(nums)

        arr = [[] for _ in range(n+1)]
        for num, cnt in hash_map.items():
            arr[cnt].append(num)

        res = []
        for i in range(n, 0, -1):
            if len(res) == k:
                break

            for ele in arr[i]:
                res.append(ele)
            
        return res