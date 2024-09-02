class Solution:
    def minimumChairs(self, s: str) -> int:
        people = 0  # 현재 대기실에 있는 사람 수
        max_people = 0  # 필요한 의자의 최대 개수
        
        for event in s:
            if event == 'E':
                people += 1  # 사람이 들어오면 사람 수 증가
            elif event == 'L':
                people -= 1  # 사람이 나가면 사람 수 감소
            
            max_people = max(max_people, people)  # 최대값을 업데이트
        
        return max_people