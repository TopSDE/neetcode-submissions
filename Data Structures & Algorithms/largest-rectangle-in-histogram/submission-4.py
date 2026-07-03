class Solution:
    def largestRectangleArea(self, a: List[int]) -> int:
        n = len(a)
        stack = []
        maxi = 0

        for i in range(n):
            while stack and a[stack[-1]] > a[i]:
                ele = a[stack.pop()]
                nse = i
                pse = stack[-1] if len(stack) > 0 else -1
                maxi = max(maxi, ele * (nse-pse-1))

            stack.append(i)

        while stack:
            ele = a[stack.pop()]
            nse = n
            pse = stack[-1] if len(stack) > 0 else -1
            maxi = max(maxi, ele * (nse-pse-1))

        return maxi