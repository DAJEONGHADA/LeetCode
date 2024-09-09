class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reversed_num = int("".join(reversed(str(num))))
        reversed_rev = int("".join(reversed(str(reversed_num))))
        return num == reversed_rev
