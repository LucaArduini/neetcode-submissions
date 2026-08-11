class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            # (l + r) // 2 can lead to overflow
            i = l + ((r - l) // 2)

            if nums[i] < nums[r]:
                r = i
            else: # nums[i] >= nums[r]
                l = i + 1
        
        return nums[l]
