class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        answer = 0
        sum_grid = sum(grid, [])
        for i in sum_grid:
            if i < 0:
                answer += 1
        return answer