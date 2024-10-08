class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quater = len(arr) / 4
        c = Counter(arr)
        answer = 0
        for num, cnt in c.items():
            if cnt > quater:
                answer = num  # 조건을 만족할 때마다 answer를 업데이트
        return answer
    
