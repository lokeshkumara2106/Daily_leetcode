class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        val=min(need1*cost1 + need2*cost2,max(need1,need2)*costBoth)
        if need1==need2:
            val=min(val,costBoth*(max(need1,need2)))
        elif need1>need2:
            val=min(val,need2*costBoth + (need1-need2)*cost1)
        else:
            val=min(val,need1*costBoth + (need2-need1)*cost2)
        return val