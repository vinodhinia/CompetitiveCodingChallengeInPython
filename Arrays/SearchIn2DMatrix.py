class Solution:
    def searchMatrixNaive(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #Time Complexity  => O(rc)
        rows = len(matrix)
        col = len(matrix[0])

        for r in range(0, rows):
            for c in range(0, col):
                if matrix[r][c] == target:
                    return True
        return False

    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        col = len(matrix[0])
        r = 0
        c = col-1

        while r < rows and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1

        return False



matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

s = Solution()
print(s.searchMatrixNaive(matrix, 3))
print(s.searchMatrix(matrix, 3))

print(s.searchMatrixNaive(matrix, 23))
print(s.searchMatrix(matrix, 23))


print(s.searchMatrixNaive(matrix, 8))
print(s.searchMatrix(matrix, 8))