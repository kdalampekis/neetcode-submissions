class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        print(len(matrix))
        target_row = 0
        for i in range(len(matrix)) :
            low = matrix[i][0]
            high = matrix[i][-1]
            if target >= low and target <= high:
                target_row = i
                print(target_row)
                break
        low = 0
        high = len(matrix[0]) - 1
        while low <= high:
            mid = (high + low) // 2
            print(mid)
            if matrix[target_row][mid] == target:
                return True
            elif target < matrix[target_row][mid]:
                high = mid - 1
            else:
                low = mid + 1
        return False