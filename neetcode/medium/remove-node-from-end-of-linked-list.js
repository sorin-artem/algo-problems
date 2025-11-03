// /**
class ListNode {
  constructor(val = 0, next = null) {
    this.val = val;
    this.next = next;
  }
}

class Solution {
  /**
   * @param {ListNode} head
   * @param {number} n
   * @return {ListNode}
   */
  removeNthFromEnd(head, n) {
    let first = head;
    let length = 0;
    let cur = head;
    while (cur) {
      length += 1;
      cur = cur.next;
    }
    const indexToRemove = length - n;
    cur = first;
    if (indexToRemove === 0) {
      return first.next;
    }
    for (let i = 0; i < length; i++) {
      if (i === indexToRemove - 1) {
        cur.next = cur.next.next;
        break;
      }
      cur = cur.next;
    }
    return first;
  }
}

// Test case: [1,2,3,4], n = 2
const head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
head.next.next.next = new ListNode(4);

const n = 2;
const solution = new Solution();
const result = solution.removeNthFromEnd(head, n);

let values = [];
let node = result;
while (node) {
  values.push(node.val);
  node = node.next;
}
console.log(values);
