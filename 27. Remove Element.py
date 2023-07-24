class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize two pointers i and j
        i = 0
        
        # Iterate through the elements in nums
        for j in range(len(nums)):
            # If the current element is not equal to val, move it to the left side of the list
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        
        # Return the new length of the list after removing all instances of val
        return i