class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        answer = 0
        collections = set()
        target = set([x + 1 for x in range(k)])
        
        while nums:
            poped_num = nums.pop()
            collections.add(poped_num)           
            answer += 1
            
            if target.intersection(collections) == target:
                break
            
        return answer