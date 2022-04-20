"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = l1
        node1 = l2
        list_l1 = []
        list_l2 = []
        while node is not None:
            list_l1.append(node.val)
            node = node.next
        while node1 is not None:
            list_l2.append(node1.val)
            node1 = node1.next
        reverse_l1 = ''.join(str(i) for i in list_l1[::-1])
        reverse_l2 = ''.join(str(j) for j in list_l2[::-1])
        new_sum = str(int(reverse_l1) + int(reverse_l2))
        new_list = []
        for i in new_sum:
            new_list.append(int(i))
        new_list = new_list[::-1]
        return_node = ListNode(val=new_list[0])
        current_node = return_node
        for j in range(1, len(new_list)):
            current_node.next = ListNode(val=new_list[j])
            current_node = current_node.next
        return return_node

