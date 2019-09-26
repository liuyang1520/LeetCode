"""
@difficulty: medium
@tags: DP
@notes: dp[i] = if put book in next line: dp[i-1] + books[i-1][1]
                else find the min(dp[j] + max_height_of_i_to_j) when the width fits
"""
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        dp = [float('inf')] * (len(books) + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            dp[i] = dp[i-1] + books[i-1][1]
            width, height = books[i-1]
            for j in range(i-1, 0, -1):
                width += books[j-1][0]
                if width > shelf_width:
                    break
                height = max(height, books[j-1][1])
                dp[i] = min(dp[i], dp[j-1] + height)
        return dp[-1]
