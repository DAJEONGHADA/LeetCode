class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = set()
        tmp = ""
        for c in word:
            if c.isnumeric():
                tmp += c
            elif tmp:
                nums.add(int(tmp))
                tmp = ""
        if tmp:
            nums.add(int(tmp))
        return len(nums)
        
        
        
        
        
        
        
        
        
        
        # # 정규 표현식을 사용하여 숫자 문자열 추출
        # numbers = re.findall(r'\d+', word)
        # # 숫자 문자열을 정수로 변환하고 집합에 저장하여 중복 제거
        # unique_numbers = {int(number) for number in numbers}
        # # 고유한 숫자의 개수를 반환
        # return len(unique_numbers)
        
        