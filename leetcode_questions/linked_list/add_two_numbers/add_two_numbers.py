from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Add two numbers represented as linked lists.
        
        Args:
            l1: First linked list representing a number in reverse order
            l2: Second linked list representing a number in reverse order
            
        Returns:
            A linked list representing the sum of the two numbers in reverse order
        """
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        
        while l1 or l2 or carry:
            # Get values from current nodes or 0 if node is None
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            
            # Calculate sum and carry
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            
            # Create new node with digit value
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            
            # Move to next nodes if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummyHead.next

# Test cases
def create_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    print(linked_list_to_list(result))  # [7, 0, 8]
    
    # Example 2
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    print(linked_list_to_list(result))  # [0]
    
    # Example 3
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    print(linked_list_to_list(result))  # [8, 9, 9, 9, 0, 0, 0, 1] 