class Solution {
  /**
   * @param {number[]} nums
   * @param {number} k
   * @return {number[]}
   */
  maxSlidingWindow(nums, k) {
    const q = [];
    const res = [];
    let l = 0;
    let r = 0;

    while (r < nums.length) {
      while (q.length > 0 && nums[q[q.length - 1]] < nums[r]) {
        q.pop();
      }
      q.push(r);
      if (l > q[0]) {
        q.shift();
      }

      if (r - l + 1 === k) {
        res.push(nums[q[0]]);
        l += 1;
      }
      r += 1;
    }
    return res;
  }
}

console.log(new Solution().maxSlidingWindow([1, 3, 1, 2, 0, 5], 3));
