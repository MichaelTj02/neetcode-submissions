class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        fleet = 0
        posToTime = []
        stack = []
        i = 0
        for i in range(0, n):
            time = (target - position[i])/speed[i]
            posToTime.append((position[i], time))
        posToTime.sort(reverse=True)

        stack.append(posToTime[0])
        for i in range(1, n):
            if posToTime[i][1] > stack[-1][1]:
                stack.append(posToTime[i])
        return len(stack)