class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_high = max(piles)
        k = k_high
        k_low = 1
        while k_low <= k_high:
            mid = (k_low + k_high) // 2
            total_hours = 0
            valid = True
            for i in range(len(piles)):
                hours = (piles[i] + mid - 1) // mid
                total_hours += hours
                if (total_hours > h):
                    valid = False
                    break
            if (valid == True):
                k = mid
                k_high = mid - 1
            else:
                k_low = mid + 1
        return k
        