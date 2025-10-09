class Solution {
  /**
   * @param {string} s
   * @param {string} t
   * @return {string}
   */
  minWindow(s, t) {
    const tMap = {};
    let totalElements = 0;
    for (const el of t) {
      totalElements += 1;
      if (el in tMap) {
        tMap[el] += 1;
      } else {
        tMap[el] = 1;
      }
    }
    let l = 0;
    let res = null;
    let curRes = "";
    const resSet = new Set();
    let currentWindow = {};
    const tSet = new Set(t);
    for (let r = 0; r < s.length; r += 1) {
      curRes = s.slice(l, r + 1);

      if (s[r] in currentWindow) {
        currentWindow[s[r]] += 1;
      } else {
        currentWindow[s[r]] = 1;
      }
      if (s[r] in tMap && currentWindow[s[r]] === tMap[s[r]]) {
        resSet.add(s[r]);
      }
      while (resSet.size === tSet.size && l <= r) {
        const newRes = s.slice(l, r + 1);
        if (res === null || (res && newRes.length < res.length)) {
          res = newRes;
        }
        currentWindow[s[l]] -= 1;
        if (s[l] in tMap && currentWindow[s[l]] < tMap[s[l]]) {
          resSet.delete(s[l]);
        }
        l += 1;
      }
    }
    console.log(tMap);
    return res === null ? "" : res;
  }
}

new Solution().minWindow("a", "a");

