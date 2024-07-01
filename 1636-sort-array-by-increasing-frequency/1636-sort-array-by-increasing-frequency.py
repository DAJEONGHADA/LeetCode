# sorted, counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        print(sorted(nums, key=lambda x: c[x]))
        print(sorted(nums, key=lambda x: -x))

        nums.sort(key=lambda x: (c[x], -x))
        # nums = sorted(nums, key=lambda x: -x)
        # print(nums)
        return nums