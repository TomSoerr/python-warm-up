"""
TOP project implemented in python. 
The Task: https://www.theodinproject.com/lessons/javascript-linked-lists
"""


def create_linked_list():
    """implementation of a linked list to better my python skills"""

    class LinkedList:
        """creates the head for the linked list and an iterator"""

        def __init__(self):
            self.head = None

        def iterator(self):
            """iterate over the linked list and returns each node"""

            tmp = self.head
            if tmp is None:
                yield None

            while tmp is not None:
                yield tmp
                tmp = tmp.next

    linked_list = LinkedList()

    class Node:
        """creates a new node for the linked list"""

        def __init__(self):
            self.value = None
            self.next = None

        def __repr__(self):
            return f'"value": {self.value}; "next": {self.next}'

    def append(value):
        """append(value) adds a new node containing value to the end of the list"""

        new_node = Node()
        new_node.value = value
        last_node = get_tail()

        if last_node is not None:
            last_node.next = new_node
        else:
            linked_list.head = new_node

    def prepend(value):
        """prepend(value) adds a new node containing value to the start of the list"""

        linked_list_iterator = linked_list.iterator()

        new_node = Node()
        new_node.value = value
        first_node = next(linked_list_iterator, None)

        if first_node is not None:
            new_node.next = first_node
            linked_list.head = new_node
        else:
            linked_list.head = new_node

    def get_size():
        """get_size() returns the total number of nodes in the list"""
        converted_list = list(linked_list.iterator())
        if len(converted_list) == 1 and converted_list[0] is None:
            return 0
        return len(converted_list)

    def get_head():
        """get_head() returns the first node in the list"""

        return linked_list.head

    def get_tail():
        """get_tail() returns the last node in the list"""

        linked_list_iterator = linked_list.iterator()

        # What if the list is empty
        for node in linked_list_iterator:
            if node is not None and node.next is None:
                return node
            if node is None:
                return node

    def at_index(index):
        """at_index(index) returns the node at the given index"""

        linked_list_iterator = linked_list.iterator()
        counter = 0

        for node in linked_list_iterator:
            if node is not None and index == counter:
                return node
            if node is None:
                return None
            counter += 1

    def pop():
        """pop() removes the last element from the list"""

        linked_list_iterator = linked_list.iterator()
        tmp = None

        for node in linked_list_iterator:
            if node is not None and node.next is None:
                if tmp is not None:
                    tmp.next = None
                else:
                    linked_list.head = None
                return node
            if node is None:
                return None
            tmp = node

    def contains(value):
        """contains(value) returns true if the passed in value is in the list and otherwise returns false"""

        linked_list_iterator = linked_list.iterator()

        for node in linked_list_iterator:
            if node is not None and node.value == value:
                return True
        return False

    def find(value):
        """
        find(value) returns the index of the node containing value, or null if not found
        """

        linked_list_iterator = linked_list.iterator()
        counter = 0

        for node in linked_list_iterator:
            if node is not None and node.value == value:
                return counter
            if node is None:
                return None
            counter += 1
        return None

    def to_string():
        """
        toString represents your LinkedList objects as strings, so you can
        print them out and preview them in the console. The format should be:
        head -> ( value ) -> ( value ) -> ( value ) -> null
        """

        linked_list_iterator = linked_list.iterator()
        string = "head -> "

        if linked_list.head is None:
            return string + "null"
        for node in linked_list_iterator:
            string += f"({node.value}) -> "
        return string + "null"

    return {
        "append": append,
        "to_string": to_string,
        "get_tail": get_tail,
        "prepend": prepend,
        "get_size": get_size,
        "get_head": get_head,
        "at_index": at_index,
        "pop": pop,
        "contains": contains,
        "find": find,
    }


def main():
    """function to load"""
    print(f"\nThe main() function got called\nFile Name: {__file__}\n")


if __name__ == "__main__":
    main()
