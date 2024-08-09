class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        answer = 0
        for type_, color, name in items:
            if ruleKey == "type" and type_ == ruleValue:
                answer += 1
            elif ruleKey == "color" and color == ruleValue:
                answer += 1
            elif ruleKey == "name" and name == ruleValue:
                answer += 1
            
        return answer