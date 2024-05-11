
# ListNode Class -- Singly Linked List

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f"List Node {repr{self.data}} --> {str(self.next)}"


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            