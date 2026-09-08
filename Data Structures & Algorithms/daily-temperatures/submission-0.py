class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        res = [0] * length
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stack_i = stack[-1][0]
                res[stack_i] = i - stack_i
                stack.pop()
            stack.append((i, t))

        return res