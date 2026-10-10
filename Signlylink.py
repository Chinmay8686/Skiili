class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def create_list(self, values):  
        self.head = None
        for value in values:
            self.insert_at_end(value)

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node

    def traverse(self):
        curr = self.head
        if curr is None:
            print("Linked list is empty")
            return

        values = []
        while curr is not None:
            values.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(values))

    def insert_at_position(self, position, value):
        new_node = Node(value)

        if position <= 1 or self.head is None:
            new_node.next = self.head
            self.head = new_node
            return

        curr = self.head
        index = 1
        while curr.next is not None and index < position - 1:
            curr = curr.next
            index += 1

        new_node.next = curr.next
        curr.next = new_node

    def find_middle(self):
        if self.head is None:
            return None

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    def delete_node(self, value):
        if self.head is None:
            print("Linked list is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        prev = self.head
        curr = self.head.next

        while curr is not None:
            if curr.data == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

        print(f"Value {value} not found in the list")

    def reverse(self):
        prev = None
        curr = self.head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    def sum_of_consecutive_pairs(self):
        curr = self.head
        sums = []

        while curr is not None and curr.next is not None:
            sums.append(curr.data + curr.next.data)
            curr = curr.next.next

        return sums


if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.create_list([10, 20, 30, 40, 50, 60])

    print("Original list:")
    ll.traverse()

    ll.insert_at_position(3, 25)
    print("After inserting 25 at position 3:")
    ll.traverse()

    middle = ll.find_middle()
    print(f"Middle node value: {middle}")

    ll.delete_node(30)
    print("After deleting 30:")
    ll.traverse()

    ll.reverse()
    print("After reversing the list:")
    ll.traverse()

    result = ll.sum_of_consecutive_pairs()
    print("Sum of every two consecutive nodes:", result)
