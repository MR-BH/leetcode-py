class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 这个重载 Comparable 的技巧要掌握
ListNode.__lt__ = lambda a, b: a.val < b.val
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
      cur = dummy = ListNode()
      pq = [head for head in lists if head]
      heapify(pq)
      while pq:
        head = heappop(pq)
        cur.next = head
        cur = cur.next
        if head.next:
          heappush(pq, head.next)
      return dummy.next

# 一个经典的分治题
class Solution:
    def mergeTwoLists(self, list1, list2):
      head = pummy = ListNode()
      while list1 and list2:
        if list1.val > list2.val:
          list1, list2 = list2, list1
        head.next = list1
        list1 = list1.next
        head = head.next
      head.next = list1 if list1 else list2
      return pummy.next
    
    def merge(self, lists, l, r):
      if l == r:
        return lists[l]
      if r < l:
        return None
      m = (l + r) // 2
      return self.mergeTwoLists(self.merge(lists, l, m), self.merge(lists, m + 1, r))

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
      return self.merge(lists, 0, len(lists)-1)
