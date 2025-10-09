/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var findTargetSumWays = function (nums, target) {
  function backtrack(i, curSum) {
    if (i === nums.length) {
      if (curSum === target) {
        return 1;
      }
      return 0;
    }
    return (
      backtrack(i + 1, curSum + nums[i]) + backtrack(i + 1, curSum - nums[i])
    );
  }

  return backtrack(0, 0);
};

console.log(findTargetSumWays([1, 1, 1, 1, 1], 3));
