class Solution:
    def minTimeToType(self, word: str) -> int:
        # 알파벳을 숫자로 표현  (ord 함수 사용)
        # 다음 글자를 입력하기 위해서 가장 빠른 방향으로 이동
        answer = 0
        loc = 0
        for c in word:
            target_loc = ord(c) - 97
            move = abs(target_loc - loc)
            move_reverse = 26 - abs(target_loc - loc)
            answer += min(move, move_reverse) + 1
            loc = target_loc
            #시계방향으로 움직였을 때의 이동 거리
            #반시계방향으로 움직였을 떄의 이동거리
            # 이 둘을 각각 구한 다음, 더 작은 거리로 이동 및 answer에 추가
            # 이동 후에는 loc 값 업데이트
            print(c, ord(c))
        return answer