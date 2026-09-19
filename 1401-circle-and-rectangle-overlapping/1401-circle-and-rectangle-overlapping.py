class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closet_x=max(x1,min(x2,xCenter))
        closet_y=max(y1,min(y2,yCenter))
        distance=(xCenter-closet_x)**2 + (yCenter-closet_y)**2
        return distance<=radius**2