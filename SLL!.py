
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Create a linked list
    def create_list(self, values):
        self.head = None
        for value in values:
            self.insert_at_end(value)

    # Insert node at the end
    def insert_at_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    # Display linked list
    def traverse(self):
        current = self.head

        if current is None:
            print("Linked list is empty")
            return

        while current is not None:
            print(current.data, end="")
            if current.next is not None:
                print(" -> ", end="")
            current = current.next
        print()

    # Insert node at a given position (1-based)
    def insert_at_position(self, position, value):
        if position < 1:
            print("Invalid position")
            return

        new_node = Node(value)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        index = 1

        while current is not None and index < position - 1:
            current = current.next
            index += 1

        if current is None:
            print("Invalid position")
            return

        new_node.next = current.next
        current.next = new_node

    # Find middle node
    def find_middle(self):
        if self.head is None:
            return None

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    # Delete a node by value
    def delete_node(self, value):
        if self.head is None:
            print("Linked list is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        previous = self.head
        current = self.head.next

        while current is not None:
            if current.data == value:
                previous.next = current.next
                return

            previous = current
            current = current.next

        print(f"Value {value} not found in the list")

    # Reverse linked list
    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    # Sum of consecutive pairs
    def sum_of_consecutive_pairs(self):
        current = self.head
        sums = []

        while current is not None and current.next is not None:
            sums.append(current.data + current.next.data)
            current = current.next.next

        return sums


# Main program
if __name__ == "__main__":
    ll = SinglyLinkedList()

    ll.create_list([10, 20, 30, 40, 50, 60])

    print("Original list:")
    ll.traverse()

    ll.insert_at_position(3, 25)
    print("After inserting 25 at position 3:")
    ll.traverse()

    print("Middle node value:", ll.find_middle())

    ll.delete_node(30)
    print("After deleting 30:")
    ll.traverse()

    ll.reverse()
    print("After reversing the list:")
    ll.traverse()

    result = ll.sum_of_consecutive_pairs()
    print("Sum of every two consecutive nodes:", result)
