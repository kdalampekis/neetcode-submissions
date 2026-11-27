class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if we can find how many times the matrix was rotated then we have the answer because lest say it was rotated 4 times then the min element is num[rotations]
        # so the key is to find the rotation in order to find the rotation we need to search where is the first element that is smaller than the nums[0].
        # So the we now the target we know also the 
        low = 0
        high = len(nums) - 1
        if (nums[low] <= nums[high]):
            return nums[low]
        while low <= high:
            mid = (low + high) // 2
            if (nums[0] > nums[mid] and nums[mid] < nums[mid-1]):
                return nums[mid]
            elif (nums[0] > nums[mid]):
                high = mid - 1
            else:
                low = mid + 1
        return nums[mid]
        