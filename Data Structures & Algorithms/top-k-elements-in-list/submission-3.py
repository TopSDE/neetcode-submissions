class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)

        hash={}
        freq=[[] for i in range(n+1)]

        for  i in nums:
            hash[i]=hash.get(i,0)+1

        for n,c in hash.items():
            freq[c].append(n)
        
        res=[]

        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res
                
                
        