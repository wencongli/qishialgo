‘’’
Runtime: 44 ms, faster than 98.11% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Trapping Rain Water.
‘’’

class Solution:
    def trap(self, height: List[int]) -> int:
        # from other's idea
        n=len(height)
        if (n<3):
            return 0
        
        # first, find the index of the highest bar
        highest_h=0
        highest_ind=-1
        for i in range(n):
            if height[i]>highest_h:
                highest_h=height[i]
                highest_ind=i
        
        water=0
        left_peak, right_peak = 0, 0
        # scan from left to right
        for i in range(highest_ind):
            if(height[i]>left_peak):
                left_peak=height[i]
            else:
                water+=left_peak-height[i]
        
        # scan from right to left
        for i in range(n-1, highest_ind, -1):
            if(height[i]>right_peak):
                right_peak=height[i]
            else:
                water+=right_peak-height[i]
                
        return water
