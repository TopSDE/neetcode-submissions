class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        st = set()
        L, R = 0, 0

        for R in range(N):
            if R - L > k:
                st.remove(nums[L])
                L += 1

            if nums[R] in st:
                return True

            st.add(nums[R])

        return False