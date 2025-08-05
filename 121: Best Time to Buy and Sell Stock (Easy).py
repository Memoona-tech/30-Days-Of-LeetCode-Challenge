# Solution 1
# ------------------------ O(n) TC ---- O(1) SC ------------

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_prof = 0

        for p in prices:
            # Compute possible profit if sold today
            potential = p - min_price
            max_prof = max(max_prof, potential)
            
            # Update minimum price seen so far for buying
            if p < min_price:
                min_price = p

        return max_prof  # If no better profit found, returns 0


# Solution 2
# -------------------- O(n) TC ---------- O(1) SC ----------

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        max_prof = 0

        for p in reversed(prices):
            max_prof = max(max_prof, max_price - p)
            max_price = max(max_price, p)

        return max_prof
