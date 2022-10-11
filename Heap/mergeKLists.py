# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i))
                lists[i] = lists[i].next
        dummy = ListNode()
        tail = dummy
        while min_heap:
            val, i = heapq.heappop(min_heap)
            tail.next = ListNode(val)
            tail = tail.next
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i))
                lists[i] = lists[i].next
        return dummy.next
        
        
        
        #brute force
        
#         if not lists:
#             return None
#         while len(lists) > 1:
#             mergedList = []
#             for i in range(0,len(lists),2):
#                 list1 = lists[i]
#                 list2 = lists[i+1] if i+1 <len(lists) else None
#                 temp = self.mergeTwoLists(list1,list2)
#                 mergedList.append(temp)
#             lists = mergedList
#         return lists[0]
    
#     def mergeTwoLists(self,list1,list2):
#             dummy = ListNode()
#             tail = dummy
            
#             while list1 and list2:
#                 if list1.val < list2.val:
#                     tail.next = list1
#                     list1 = list1.next
#                 else:
#                     tail.next = list2
#                     list2 = list2.next
#                 tail = tail.next
            
#             if list1:
#                 tail.next = list1
#             if list2:
#                 tail.next = list2
#             return dummy.next