class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # 1차원 배열의 길이가 m*n과 같지 않다면 빈 배열 반환
        if len(original) != m * n:
            return []
        
        answer = []
        # 0부터 len(original)까지 n 간격으로 반복하면서 슬라이싱
        for i in range(0, len(original), n):
            # i부터 i+n까지 잘라서 행(row) 생성
            row = original[i:i+n]
            answer.append(row)
        
        return answer