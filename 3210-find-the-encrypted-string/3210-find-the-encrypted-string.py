class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        answer = ""
        for i in range(len(s)):
            answer += s[(i+k) % len(s)]
        return answer