class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=x
        while(left<right):
            mid=(left+right+1)>>1
            if mid<=x//mid:
                left=mid
            else:
                right=mid-1
        return left