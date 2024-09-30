class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # answer = ""
        # if ch in word:
        #     idx = word.index(ch)
        #     for i in range(idx, -1, -1):
        #         answer += word[i]
        #     return answer + word[idx+1:]
        # else:
        #     return word

        
        if ch not in word:
            return word
        
        # ch가 처음 나타나는 위치를 찾음
        chr_index = word.index(ch)
        
        # 접두사 부분을 뒤집고 나머지 문자열과 합침
        return word[:chr_index+1][::-1] + word[chr_index+1:]
