class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(value)
    
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print("None")
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def merge_sort(self):
        def split(head):
            if not head or not head.next:
                return head, None
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            middle = slow.next
            slow.next = None
            return head, middle
        
        def merge(left, right):
            if not left:
                return right
            if not right:
                return left
            if left.value < right.value:
                left.next = merge(left.next, right)
                return left
            else:
                right.next = merge(left, right.next)
                return right
        
        def merge_sort_recursive(head):
            if not head or not head.next:
                return head
            left, right = split(head)
            left = merge_sort_recursive(left)
            right = merge_sort_recursive(right)
            return merge(left, right)
        
        self.head = merge_sort_recursive(self.head)
    
    @staticmethod
    def merge_sorted_lists(list1, list2):
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.value < list2.value:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next

# Тест
ll = LinkedList()
for val in [4, 2, 5, 1, 3]:
    ll.append(val)
print("Original list:")
ll.print_list()

print("Reversed list:")
ll.reverse()
ll.print_list()

print("Sorted list:")
ll.merge_sort()
ll.print_list()

ll1 = LinkedList()
ll2 = LinkedList()
for val in [1, 3, 5]:
    ll1.append(val)
for val in [2, 4, 6]:
    ll2.append(val)

print("Merged sorted lists:")
merged_head = LinkedList.merge_sorted_lists(ll1.head, ll2.head)
merged_list = LinkedList()
merged_list.head = merged_head
merged_list.print_list()


ll3 = LinkedList()
ll4 = LinkedList()
for val in [10, 20, 30]:
    ll3.append(val)
for val in [5, 15, 25]:
    ll4.append(val)

print("Merged another sorted lists:")
merged_head2 = LinkedList.merge_sorted_lists(ll3.head, ll4.head)
merged_list2 = LinkedList()
merged_list2.head = merged_head2
merged_list2.print_list()

ll5 = LinkedList()
for val in [7, 3, 9, 2, 8]:
    ll5.append(val)
print("Unsorted list:")
ll5.print_list()
print("Sorted list:")
ll5.merge_sort()
ll5.print_list()