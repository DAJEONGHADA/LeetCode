class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        answer = 0
        for sentence in sentences:
            word_count = len(sentence.split())
            if word_count > answer:
                answer = word_count
        return answer