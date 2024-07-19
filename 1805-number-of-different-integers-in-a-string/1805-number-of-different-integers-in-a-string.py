class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        # tmp = ""
        # for c in word:
        #     if c.isnumeric():
        #         tmp += c
        #     elif tmp:
        #         print(tmp)
        #         tmp = ""
        #     if tmp:
        #         print(tmp)
        #     return 0
        
        numbers = re.findall(r'\d+', word)
        # 숫자 앞의 0을 제거하고 정수로 변환하여 집합에 추가
        unique_numbers = {int(number) for number in numbers}
        return len(unique_numbers)
        
        
        