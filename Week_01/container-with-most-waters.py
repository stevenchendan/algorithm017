# https://leetcode.com/problems/container-with-most-water/submissions/
# solution 1: two pointer
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        i = 0
        j = len(height) - 1
        res = 0
        # two pointer
        while i < j:
            # move the side which will not reduce the total area
            res = max(res, min(height[i], height[j]) * (j - i))
            if (height[i] <= height[j]):
                i += 1
            else:
                j -= 1
        return res
        
        #solution 2: brute force   (exceed time limit)
#         area = 0
#         for i in range(0, len(height) - 1):
#             for j in range(i+1, len(height)):
#                 area = min(height[i], height[j]) * (j - i)
#                 if (area > res):
#                     res = area
#         return res