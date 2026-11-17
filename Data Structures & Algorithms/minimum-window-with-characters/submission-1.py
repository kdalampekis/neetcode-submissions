class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""

        need = {}                          # letter → how many t needs
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}                        # letter → how many are in the current window
        have = 0                           # how many distinct letters of t are fully covered
        required = len(need)               # how many distinct letters must be covered

        best_len = float("inf")
        best_left = 0
        left = 0

        for right in range(len(s)):
            c = s[right]                   # letter enters on the right
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                have += 1                  # this letter just reached the count t needs

            while have == required:        # the window covers t
                if right - left + 1 < best_len:          # shorter than the best so far
                    best_len = right - left + 1
                    best_left = left
                d = s[left]                # letter leaves on the left
                window[d] -= 1
                if d in need and window[d] < need[d]:
                    have -= 1              # this letter is no longer covered
                left += 1

        return "" if best_len == float("inf") else s[best_left:best_left + best_len]