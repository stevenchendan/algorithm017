# https://leetcode.com/problems/climbing-stairs/
# 动态规划
class Solution:
  def climbStairs(self, n: int) -> int:
    if n < 0:
      return 0
    result = [1, 1]
    for i in range(2, n+1):
      result.append(result[i-1] + result[i - 2])
    return result[n]

