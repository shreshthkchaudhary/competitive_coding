# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev












        # # sem: 2
        # prev = None
        # curr = head

        # while curr is not None:
        #     next_node = curr.next
        #     curr.next = prev 
        #     prev = curr
        #     curr = next_node

        # return prev















        # temp = head
        # temp2 = head
        # s=[]
        # while temp != None:
        #     s.append(temp.val)
        #     temp==temp.next
        # for i in s[::-1]:
        #     temp2.val == i
        #     temp2=temp2.next
        # return head


        # current= head
        # pev= None
        # while current != None:
        #     nextnode=current.next
        #     current.next=pev
        #     pev=curren            current=nextnode






        # temp2 = head
        # s=()
        # while temp != None:
        #     pev == temp
        #     temp==temp.next

        
        # while temp != None:
        #     temp.next==temp
        #     temp==temp.next
        # return pev