/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
  if (height == null || height.height == 0) {
      return null;
  }
  i = 0;
  j = height.length - 1;
  result = 0;
  //two pointer
  while (i < j) {
      if (height[i] <= height[j]) {
          result = Math.max(result, height[i] * (j - i));
          i += 1;
      }
      else {
          result = Math.max(result, height[j] * (j - i));
          j -= 1;
      }
  }
  return result;
};