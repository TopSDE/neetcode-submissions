class Solution:
    def largestRectangleArea(self, a: List[int]) -> int:
        n = len(a)
        ans = -1

        for i in range(n):
            max_area = a[i]
            min_ele = a[i]

            for j in range(i+1, n):
                min_ele = min(min_ele, a[j])
                max_area = max(max_area, min_ele * (j-i+1))

            ans = max(ans, max_area)

        return ans