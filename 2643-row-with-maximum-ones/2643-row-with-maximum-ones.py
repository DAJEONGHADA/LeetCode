class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        # for, count
        
        data = []
        for i, row in enumerate(mat):
            one_cnt = row.count(1)
            data.append([i, one_cnt])
#             sorted를 적용해서 가장 앞에 있는 element 리턴!
            data_sorted = sorted(data, key=lambda x: x[1], reverse=True)
        return data_sorted[0]