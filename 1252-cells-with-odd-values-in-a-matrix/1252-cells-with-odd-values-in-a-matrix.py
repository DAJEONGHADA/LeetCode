class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0 for x in range(n)] for y in range(m)]

        answer = 0
        for row, col in indices:
            for i in range(n): 
                matrix[row][i] += 1
            for i in range(m):
                matrix[i][col] += 1 
                
        for i in range(m):
            for j in range(n):
                if matrix[i][j] % 2 == 1:
                    answer += 1
        
        return answer