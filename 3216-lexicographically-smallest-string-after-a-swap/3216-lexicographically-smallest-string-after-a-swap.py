class Solution:
    def getSmallestString(self, s: str) -> str:
#         1. 반목문을 돌면서 인접한 두 글자가 모두 짝수이거나 모두 홀수인 경우
#         2. swqp을 수행해서 새로운 문자열을 만든다.
#         3. 새로 만든 문자열을 candidates라는 list에 추가한다.
#         4. candidates를 정렬한 다음, 가장 앞에 오는 수를 리턴한다.

        answer = [s]
        for i in range(len(s) - 1):
            if int(s[i]) % 2 == int(s[i+1]) % 2:
                swaped = s[:i] + s[i+1] + s[i] + s[i+2:]
                print(s[i], s[i+1], swaped)
                answer.append(swaped)
        return sorted(answer)[0]