class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        answer = 0
        n = len(mat)
        for i in range(n):
            answer += mat[i][i]
            answer += mat[i][n-1-i]
        # 한변의 길이가 홀수일 때는 겹치는 중간값 한번 빼주기
        if n % 2 == 1:
            answer -= mat[n//2][n//2]
        return answer