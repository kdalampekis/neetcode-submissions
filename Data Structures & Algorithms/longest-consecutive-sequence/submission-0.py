class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set()
        for n in nums:
            mySet.add(n)

        max_length  = 0
        
        for n in nums:
            length = 1
            if n -1 not in mySet:
                while n+1 in mySet:
                    length +=1 
                    n = n + 1
                if length > max_length:
                    max_length = length
            else:
                continue

        return max_length