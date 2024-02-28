from typing import optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
#time complexity =O(n)  space complexity = O(n)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> optional[ListNode]:
    # Define a hash set to store nodes
    visited_nodes = set()

    # Traverse the first linked list and store nodes in the hash set
    while headA:
        visited_nodes.add(headA)
        headA = headA.next

    # Traverse the second linked list and check for intersection
    while headB:
        if headB in visited_nodes:
            return headB
        headB = headB.next

    # No intersection found
    return None
'''

#time complexity = O(n) space complexity = O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> optional[ListNode]:
        #calculate length of both linked list
        def length_of_list(node):
            length=0
            while node:
                node=node.next
                length+=1
            return length
        
        a=length_of_list(headA)
        b=length_of_list(headB)
        while a>b:
            headA=headA.next
            a-=1
        while b>a:
            headB=headB.next
            b-=1   
        #find intersection
        while headA and headB:
            if (headA==headB): return headA
            headA=headA.next
            headB=headB.next
        return None
    