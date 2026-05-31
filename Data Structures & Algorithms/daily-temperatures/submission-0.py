class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0] * n

        for idx in range(n-1, -1, -1):
            while stack and temperatures[idx] >= temperatures[stack[-1]]:
                stack.pop()

            ans[idx] = stack[-1] - idx if stack else 0
            stack.append(idx)

        return ans