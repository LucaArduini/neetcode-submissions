class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h: number of hours you have to eat all the bananas.
        # k: bananas-per-hour eating rate

        k = 1
        while 1:
            sum = 0
            for x in piles:
                sum += ((x + k - 1) // k)  # equivalente di: math.ceil(pile / k)
            
            if sum <= h:
                return k
            # else:
            k += 1

        return -1
