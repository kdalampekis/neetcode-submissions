class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()      # characters currently in the window
        left = 0          # left edge of the window
        best = 0          # longest valid window seen so far

        for right in range(len(s)):          # right edge moves one step each time
            while s[right] in seen:          # duplicate: drop from the left
                seen.remove(s[left])         # until the old copy is gone
                left += 1
            seen.add(s[right])
            best = max(best, right - left + 1)

        return best