class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permut_s1 = defaultdict(int)
        permut_s2 = defaultdict(int)
        for c in s1:
            permut_s1[c] += 1
        for i in range(len(s2)):
            j = i
            while s2[j] in s1 and (permut_s2[s2[j]]<permut_s1[s2[j]]):
                permut_s2[s2[j]] += 1
                if j < len(s2) - 1:
                    j += 1
                else: 
                    break
            if( permut_s1 == permut_s2):
                return True
            else:
                permut_s2.clear()

        return False



