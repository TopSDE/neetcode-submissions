class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        st = set()
        res = 0

        l, r = 0, 0
        while r < N:
            if s[r] in st:
                res = max(res, (r - l))

                while s[l] != s[r]:
                    st.remove(s[l])
                    l += 1

                st.remove(s[l])
                l += 1

            st.add(s[r])
            r += 1

        res = max(res, r - l)
        return res