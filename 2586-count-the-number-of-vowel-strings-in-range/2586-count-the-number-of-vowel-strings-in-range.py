class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        answer = 0
        vowel = ["a", "e", "i", "o", "u"]
        
        for i in range(left, right+1):
            word = words[i]
            if word[0] in vowel and word[-1] in vowel:
                answer += 1
                
        return answer
