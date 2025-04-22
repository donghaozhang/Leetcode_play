from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into one sorted list.
        
        Args:
            list1: First sorted linked list
            list2: Second sorted linked list
            
        Returns:
            The head of the merged sorted linked list
        """
        # Create a dummy head node
        dummy = ListNode(-1)
        current = dummy
        
        # Traverse both lists
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        # Attach the remaining nodes
        if list1:
            current.next = list1
        else:
            current.next = list2
            
        return dummy.next

# Helper functions for testing
def create_linked_list(values):
    dummy = ListNode(-1)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
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
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(linked_list_to_list(result))  # [1, 1, 2, 3, 4, 4]
    
    # Example 2
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    print(linked_list_to_list(result))  # []
    
    # Example 3
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    print(linked_list_to_list(result))  # [0] 