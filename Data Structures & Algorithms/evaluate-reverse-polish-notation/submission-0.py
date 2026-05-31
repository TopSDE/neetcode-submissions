class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch.isnumeric() or (ch.startswith(('-')) and len(ch) >= 2):
                stack.append(ch)

            elif ch == '+':
                stack.append(str(int(stack.pop()) + int(stack.pop())))

            elif ch == '-':
                ele1 = int(stack.pop())
                ele2 = int(stack.pop())
                stack.append(str(ele2 - ele1))

            elif ch == '*':
                stack.append(str(int(stack.pop()) * int(stack.pop())))

            else:
                ele1 = int(stack.pop())
                ele2 = int(stack.pop())
                stack.append(str(int(ele2 / ele1)))

        return int(stack.pop())