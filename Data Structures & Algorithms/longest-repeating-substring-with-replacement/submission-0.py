class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)     # γράμμα → πόσες φορές είναι στο παράθυρο
        left = 0
        best = 0

        for right in range(len(s)):
            count[s[right]] += 1                       # το γράμμα μπαίνει

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1                    # το γράμμα φεύγει
                left += 1

            best = max(best, right - left + 1)

        return best