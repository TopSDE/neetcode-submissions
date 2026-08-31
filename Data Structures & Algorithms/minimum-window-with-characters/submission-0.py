class Solution:
    def minWindow(self, s: str, t: str) -> str:
        N = len(s)
        M = len(t)

        hashMapt = Counter(t)
        hashMap = {}

        have = M
        need = 0

        l = 0
        resCnt = float('inf')
        resTup = None

        for r in range(N + 1):
            while l < r and need >= have:
                if (r - l) < resCnt:
                    resCnt = r - l
                    resTup = (l, r)

                if s[l] in hashMap:
                    hashMap[s[l]] -= 1

                    if hashMap[s[l]] < hashMapt[s[l]]:
                        need -= 1

                l += 1

            if r < N and s[r] in hashMapt:
                hashMap[s[r]] = hashMap.get(s[r], 0) + 1

                if hashMap[s[r]] <= hashMapt[s[r]]:
                    need += 1

        return s[resTup[0] : resTup[1]] if resTup else ""

# class Solution:
#     def check(self, t, hashMapt, hashMap):
#         for ch in t:
#             if hashMap.get(ch, 0) < hashMapt[ch]:
#                 return False

#         return True

#     def minWindow(self, s: str, t: str) -> str:
#         N, M = len(s), len(t)

#         l = 0
#         res = float('inf')

#         hashMapt = Counter(t)
#         hashMap = {}

#         resTup = None

#         for r in range(N + 1):
#             while l < r and self.check(t, hashMapt, hashMap):
#                 if (r - l) < res:
#                     res = r - l
#                     resTup = (l, r)
                
#                 if s[l] in hashMap:
#                     hashMap[s[l]] -= 1
#                 l += 1

#             if r < N:
#                 if s[r] in hashMapt:
#                     hashMap[s[r]] = hashMap.get(s[r], 0) + 1

#         return s[resTup[0] : resTup[1]] if resTup else ''

        # Few Own Test Cases
            # AAAASBBCCCD
            # AABABCCDE
            # ABDEFAXCBC
            # ABCXASS