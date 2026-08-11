class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            # (l + r) // 2 can lead to overflow
            m = l + ((r - l) // 2)

            if nums[m] < nums[r]:
                r = m
            else: # nums[m] >= nums[r]
                l = m + 1

        pivot = l
        print("pivot found at index:", pivot, "with value:", nums[pivot])

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        if nums[0] <= target and pivot and target <= nums[pivot - 1]:
            print("cerco tra index", 0, "ed", pivot - 1)
            res = binary_search(0, pivot - 1)
        else:
            res = binary_search(pivot, len(nums) - 1)
            print("cerco tra index", pivot, "ed", len(nums) - 1)

        return res