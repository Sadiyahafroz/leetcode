class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l= []
        for n in range(len(nums)):
            if nums[n]== target:
                j = n
                l.append(target)
        
        if target in l:
            return j
        else:
            return -1