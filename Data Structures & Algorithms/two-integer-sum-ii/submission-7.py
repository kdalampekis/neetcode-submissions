class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indexes = []
        i = 0
        j = len(numbers)-1   
        while j > i:
            if numbers[i] + numbers[j] == target:
                indexes.append(i+1)
                indexes.append(j+1)
                return indexes
            if numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] < target:
                i += 1
        