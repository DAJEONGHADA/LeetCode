class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # answer = 0
        # for sentence in sentences:
        #     word_count = len(sentence.split())
        #     if len(sentence.split()) > answer:
        #         answer = word_count
        # return answer
        return max(len(sentence.split()) for sentence in sentences)
    
    
    
    
        