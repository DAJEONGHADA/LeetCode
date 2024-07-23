class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        # while 문
        # 115원을 가져가려면 75원 1개, 10원 4개가 필요
        
        answer = 0

        while True:
            if x >= 1 and y >= 4:
                x -= 1
                y -= 4
            else:
                if answer % 2 == 0:
                    return "Bob"
                else:
                    return "Alice" 

            answer += 1