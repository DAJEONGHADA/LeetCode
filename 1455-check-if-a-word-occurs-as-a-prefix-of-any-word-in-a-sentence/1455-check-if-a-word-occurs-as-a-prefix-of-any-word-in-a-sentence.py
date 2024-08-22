class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()  # 문장을 단어별로 나눔
        
        for i, word in enumerate(words):
            if word.startswith(searchWord):  # 단어가 searchWord로 시작하는지 확인
                return i + 1  # 첫 번째 일치하는 단어의 1-indexed 위치 반환
                
        return -1  # 해당하는 단어가 없으면 -1 반환