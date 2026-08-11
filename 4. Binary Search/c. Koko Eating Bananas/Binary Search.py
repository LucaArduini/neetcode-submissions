class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h: number of hours you have to eat all the bananas.
        # k: bananas-per-hour eating rate

        left = 1
        right = max(piles)

        while left < right:
            m = (left + right) // 2
            sum = 0
            for pile in piles:
                sum += ((pile + m - 1) // m)  # equivalente di: math.ceil(pile / m)
            
            if sum <= h:
                right = m
            elif sum > h:
                left = m + 1

        return left
