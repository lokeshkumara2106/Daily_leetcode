class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def getdays(date):
            monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            month=int(date[:2])
            days=int(date[3:])
            return sum(monthList[:month-1])+days
        return max(0,getdays(min(leaveAlice,leaveBob))-getdays(max(arriveAlice,arriveBob))+1)