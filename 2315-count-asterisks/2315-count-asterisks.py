class Solution:
    def countAsterisks(self, s: str) -> int:
    # split, count, for, if
        answer = 0
        word_list = s.split("|")
        for i in range(0, len(word_list), 2):
        # word_list[i] 안에 포함되어 있는 *의 개수를 세어서 
        # answer 에가다가 추가
            word_count = word_list[i].count("*")
            answer += word_count
        return answer