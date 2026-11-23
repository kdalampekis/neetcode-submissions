class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Σε καθε γυρω συνθηκης προσθετω position + speed και μετα βλεπω αν το result ειναι ιδιο για καποι αμαξι και αυτο το κανω οσο το result <= target 
        n = len(position)
        result = 0
        curr = [[] for _ in range(n)]

        for i in range(0, n):
            curr[i]=[position[i], speed[i]]
        curr.sort(reverse=True)
        curr_time = 0
        for i in range(len(curr)):
            time = (target - curr[i][0]) / curr[i][1]
            if time <= curr_time:
                continue
            else:
                result += 1
                curr_time = time
        return result
        