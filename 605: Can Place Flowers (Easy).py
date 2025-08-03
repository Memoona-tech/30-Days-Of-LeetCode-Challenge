# Solution 1
# ---------------------- O(len(flowerbed)) TC ----------------- O(1) SC ---------- 

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)

        if n == 0:
            return True

        for i in range(length):
            if flowerbed[i]==0:
                left_empty = (i==0) or (flowerbed[i-1]==0)
                right_empty = (i==length-1) or (flowerbed[i+1]==0)
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        return count >= n
