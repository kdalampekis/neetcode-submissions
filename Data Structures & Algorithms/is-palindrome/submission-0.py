class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for i in range(len(s)):
            if s[i].isalnum():
                chars.append(s[i])
        print(chars)
        n = -1
        for i in range(len(chars)):
            if chars[i].upper()   == chars[n].upper()   and i != n:
                n -=1
                continue
            if chars[i].upper()   == chars[n].upper()   and i == n:
                return True
            else:
                return False
        return True