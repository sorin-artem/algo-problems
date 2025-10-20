/**
 * Definition for singly-linked list.
 */
class ListNode {
  constructor(val = 0, next = null) {
    this.val = val;
    this.next = next;
  }
}

class Solution {
  /**
   * @param {ListNode} head
   * @return {ListNode}
   */
  reverseList(head) {
    let cur = head;

    let newNext = null;
    while (cur) {
      let temp = cur.next;
      cur.next = newNext;
      newNext = cur;
      cur = temp;
    }

    return newNext;
  }
}

// Helper function to create linked list from array
function createList(arr) {
  if (arr.length === 0) return null;
  let head = new ListNode(arr[0]);
  let current = head;
  for (let i = 1; i < arr.length; i++) {
    current.next = new ListNode(arr[i]);
    current = current.next;
  }
  return head;
}

// Create list from [0,1,2,3]
let list = createList([0, 1, 2, 3]);
console.log(list);
new Solution().reverseList(list);
