from ListNode import ListNode
import copy


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        curr_node = self.head

        output = ''
        # if populated with anything
        if curr_node is not None:
            # if populated with single value
            if curr_node.next is None:
                output += f'{curr_node.value}'
                return output
            # if there's multiple values
            # loop over all and add to output str
            else:
                while curr_node.next is not None:
                    output += f'{curr_node.value}'
                    curr_node = curr_node.next
                return output
        else:
            return "Nothing to see here!"

            # return output

    """BELOW NOT NEEDED. ALTHOUGH IT HAS PREV AND NEXT 
    POINTERS, THE STORAGE WILL FUNCTION LIKE A SINGLY 
    LINKED LIST AND SHOULD ONLY ADD TO TAIL"""

    # def add_to_head(self, value):
    #     new_node = ListNode(value)
    #     self.length += 1
    #     # if list is empty
    #     if self.head is None and self.tail is None:
    #         self.head = new_node
    #         self.tail = new_node
    #     else:
    #         new_node.next = self.head
    #         self.head.prev = new_node
    #         self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    # Below logic is handled within the delete method
    # Commented out just in case it could be useful later
    # def remove_from_head(self):
    #     self.length -= 1
    #     copy_head = copy.copy(self.head.value)
    #     # contains single value
    #     if self.head == self.tail:
    #         self.delete(self.head)
    #         return copy_head
    #     # if empty
    #     elif self.head == None and self.tail == None:
    #         return
    #     else:
    #         self.delete(self.head)
    #         return copy_head

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        self.length += 1
        new_node = ListNode(value)
        # list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        # # if length is one
        # elif self.head is self.tail:
        #     self.head.next = new_node
        #     new_node.prev = self.head
        #     self.tail = new_node
        # else:
        #     self.tail.next = new_node
        #     new_node.prev = self.tail
        #     self.tail = new_node

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):

        # if linked list has one value, meaning head == tail
        if self.head is self.tail and self.head is node:
            self.head = None
            self.tail = None
            self.length = 0
            return
        # if linked list is empty
        elif self.length is 0 and self.head is None and self.tail is None:
            return
        else:
            # if deleted node is the head
            if node.prev is None:
                self.head = node.next
                node.delete()
            # if deleted node is the tail
            elif node.next is None:
                self.tail = node.prev
                node.delete()
            else:
                node.delete()

            self.length -= 1


ll = LinkedList()
print(ll)
ll.add_to_tail(44)
print(ll)
ll.add_to_tail(45)
print(ll)
