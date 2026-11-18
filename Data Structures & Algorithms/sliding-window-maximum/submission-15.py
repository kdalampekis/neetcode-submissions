class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_element = []
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return nums
        elif k == 1:
            return nums
        # # καθε φορα θα κοιταμαι αν το πρωτο στοιχιο στο window αν δεν ειναι το μεγαλυτερο
        # απλα ελεγχουμε οτι το νεο στοιχειο που μπαινει δλδ το right ειναι μεγαλυτερο απο το max που ειχαμε μεχρι στιγμης. Αν το left ηταν το μεγαλυτερο τοτε ψαχνουμε να βρουμε το μεγαλυτερο στο νεο window... δλδ καθε φορα θα πρεπει να flagαρουμε αν το left ηταν το μεγαλυτερο στοιχειο γιατι αυτο μας δημιουργει προβλημα γιατι ειναι αυτο που βγαινει 
        left  = 0 
        max_left  = False 
        curr_max = nums[0]
        for i in range(0, k, 1):
            if nums[i] >= curr_max and left == i:
                curr_max = nums[i]
                max_left = True
            elif nums[i] >= curr_max and left != i:
                curr_max = nums[i]
                max_left = False
        max_element.append(curr_max)
        left = 1
        right = left + k - 1
        while right != len(nums):
            if max_left == False:
                curr_max = max(curr_max, nums[right])
                if left != len(nums) and nums[left] == curr_max:
                    max_left = True
                max_element.append(curr_max)
                if right != len(nums) and left != len(nums):
                    left += 1
                    right += 1
                else:
                    break
            else:
                curr_max = nums[left]
                for i in range(left, right+1, 1):
                    if nums[i] >= curr_max and left == i:
                        curr_max = nums[i]
                        max_left = True
                    elif nums[i] >= curr_max and left != i:
                        curr_max = nums[i]
                        max_left = False
                max_element.append(curr_max)
                if right != len(nums) and left!= len(nums):
                    left += 1
                    right += 1
                else:
                    break
                
        return max_element
