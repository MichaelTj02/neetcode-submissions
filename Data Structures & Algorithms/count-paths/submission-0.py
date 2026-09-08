class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cache = [-1] * n
        for i in range(0, n):
            cache[i] = [-1] * m
        for i in range (0, n):
            cache[i][0] = 1
        for i in range (0, m):
            cache[0][i] = 1

        for i in range (1, n):
            for j in range (1, m):
                cache[i][j] = cache[i-1][j] + cache[i][j-1]
        
        
        return cache[n-1][m-1]
