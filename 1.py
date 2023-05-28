#TwoSum 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            a = nums.index(i)
            for n in range(len(nums)):
                if n == a:
                    continue
                else:
                    if i + nums[n] ==target:
                        b = n
                        return a,n
               