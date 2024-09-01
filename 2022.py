# 2022. Convert 1D Array Into 2D Array
# https://leetcode.com/problems/convert-1d-array-into-2d-array

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):  
            return []
        
        arr = [[0] * n for _ in range(m)]  
        k = 0
        for i in range(m):
            for j in range(n):
                arr[i][j] = original[k]  
                k += 1
        
        return arr