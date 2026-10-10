def findCommonElements(list1, list2) -> list[int]:
    def to_list(node_or_list):
        # If it's already a list or iterable, return it as a list
        if isinstance(node_or_list, (list, set, tuple)):
            return list(node_or_list)
        
        # Otherwise, traverse the linked list (ListNode)
        res = []
        curr = node_or_list
        while curr is not None:
            res.append(curr.val)
            curr = curr.next
        return res

    l1 = to_list(list1)
    l2 = to_list(list2)
    
    # Find common elements and return as a sorted list with no duplicates
    return sorted(list(set(l1) & set(l2)))