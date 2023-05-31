class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = []
        if target in nums:
            return nums.index(target)
        else:
            l = nums.copy()
            l.append(target)
            l.sort()
            return l.index(target)

