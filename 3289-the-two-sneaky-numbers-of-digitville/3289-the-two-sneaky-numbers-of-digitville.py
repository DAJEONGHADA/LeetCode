class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        answer = []
        # 각 숫자의 빈도를 계산
        count = Counter(nums)
        
        # 빈도가 2인 숫자를 찾아서 answer에 추가
        for num, i in count.items():
            if i == 2:
                answer.append(num)
        
        return answer