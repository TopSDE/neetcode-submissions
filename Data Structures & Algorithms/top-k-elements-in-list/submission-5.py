class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = Counter(nums)

        heap = []
        for num, cnt in hash_map.items():
            heapq.heappush(heap, [cnt, num])
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res