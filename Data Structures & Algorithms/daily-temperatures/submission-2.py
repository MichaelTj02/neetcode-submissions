class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i = 0
        result = [0] * len(temperatures)
        stack = []
        while i < len(temperatures):
            curr = temperatures[i]
            if stack and curr > temperatures[stack[-1]]:
                while stack and temperatures[stack[-1]] < curr:
                    result[stack[-1]] = i - stack[-1] 
                    stack.pop()
            stack.append(i)
            i+=1
        
        return result
