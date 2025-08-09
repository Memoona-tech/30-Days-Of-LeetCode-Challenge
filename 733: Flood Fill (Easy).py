# SOLUTION 1
# ------------------ O(m×n)) TC ----------- O(m×n) SC --------

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rows, cols = len(image), len(image[0])
        original_clr = image[sr][sc] 

        if original_clr == color:
            return image
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or  c >= cols:
                return
            
            if image[r][c] != original_clr:
                return

            image[r][c] = color

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        dfs(sr, sc)
        return image
