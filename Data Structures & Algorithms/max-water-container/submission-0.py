class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = abs(j - i) * min(height[i], height[j])
        # θελουμε το j να ειναι οσο πιο μεγαλο γινεται και το υψος του οσο πιο μεγαλο γινεται παρολα αν το υψος του i ειναι μικροτερο απο του j τοτε μας νοιαζει μονο το ποσο μακρια ειναι αλλα αν το υψος του i ειναι μεγαλυτερο απο του j μας νοιαζει και το υψος του και η αποσταση 
        j = len(heights) - 1
        i = 0 
        max_area = (j - i) * min(heights[i], heights[j])
        while i < j :
            if ((j - i) * min(heights[i], heights[j])) > max_area:
                max_area = (j - i) * min(heights[i], heights[j])
            if heights[i] < heights[j]:
                i += 1
            else:
                j -=1
        return max_area
