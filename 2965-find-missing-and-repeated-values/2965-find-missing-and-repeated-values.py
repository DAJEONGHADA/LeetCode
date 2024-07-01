class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # form collections import Counter
        # 2중 for 문
        c = Counter()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                c[grid[i][j]] += 1
        answer = [-1, -1]
        
        n = len(grid)
        for i in range(1, n * n + 1):
            if c[i] == 2:
                answer[0] = i
            if c[i] == 0:
                answer[1] = i
            
        return answer