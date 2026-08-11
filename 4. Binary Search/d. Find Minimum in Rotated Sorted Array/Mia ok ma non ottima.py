class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        if nums[0] <= nums[r]:
            return nums[0]

        while l <= r:
            # (l + r) // 2 can lead to overflow
            i = l + ((r - l) // 2)

            if nums[i] > nums[l]:
                l = i +1
            elif nums[i] < nums[r]:
                r = i

            if nums[i]>nums[i+1]:
                return nums[i+1]
        
        return -1


# NB: When nums[mid] < nums[right], the minimum could be at mid itself, so set 
# right = mid (not mid - 1). 
# When nums[mid] >= nums[right], the minimum must be in the right half, so set
# left = mid + 1. Using wrong update logic either skips the minimum or causes infinite loops.