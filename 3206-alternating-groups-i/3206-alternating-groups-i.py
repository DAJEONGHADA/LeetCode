class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        answer = 0
        n = len(colors)
        
        for i in range(n):
            color_one = colors[i]
            color_two = colors[(i + 1) % n]
            color_three = colors[(i + 2) % n]
            
            # Check if we have an alternating group
            if color_one != color_two and color_two != color_three:
                answer += 1
                
        return answer