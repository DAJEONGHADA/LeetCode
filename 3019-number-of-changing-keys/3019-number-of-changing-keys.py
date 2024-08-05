# class Solution:
#     def countKeyChanges(self, s: str) -> int:
#         answer = 0
#         for i in range(1, len(s)):
#             # s의 i번째 문자의 소문자가 i-1번째 문자의 소문자와 같지 않은지
#             if s[i].lower() != s[i - 1].lower():
#                 answer += 1
#         return answer

class Solution:
    def countKeyChanges(self, s: str) -> int:
        answer = 0
        # 문자열 lower, for문 사용해서 앞에 문자와 뒤에 문자 비교
        s = s.lower()
        for i in range(len(s) - 1):
            if s[i].lower() != s[i+1].lower():
                answer += 1
        return answer