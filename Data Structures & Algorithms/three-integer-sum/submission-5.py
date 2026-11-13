class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        result = set()
        for i in range(len(nums)-2):
            j = len(nums) - 1 
            target  = - nums[i]
            k = i
            while k < j-1:
                if (nums[k+1]+nums[j]) == target:
                    result.add((nums[i], nums[k+1], nums[j]))
                    k+=1
                elif (nums[k+1]+nums[j]) > target:
                    j -= 1
                elif (nums[k+1]+nums[j]) < target:
                    k += 1
                
        return [list(t) for t in result]