class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N = len(s)
        hashMap = {}
        l, maxf, res = 0, 0, 0

        for r in range(N):
            hashMap[s[r]] = hashMap.get(s[r], 0) + 1
            maxf = max(maxf, hashMap[s[r]])
            
            if (r - l + 1) - maxf > k:
                hashMap[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)

        return res