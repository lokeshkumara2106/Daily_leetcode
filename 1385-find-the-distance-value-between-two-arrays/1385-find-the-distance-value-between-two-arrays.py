class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        total=0
        for i in range(len(arr1)):
            found=True
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])<=d:
                    found=False
                    break
            if found:
                total+=1
        return total