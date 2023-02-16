from node import Node
from LinkedList import LinkedList

class Stack:
    def __init__(self):
        self.list = LinkedList()
        
    def push(self, new_item):
        # Create a new node to hold the item
        new_node = Node(new_item)
        
        # Insert the node as the list head (top of stack)
        self.list.prepend(new_node)
    
    def pop(self):
        # Copy data from list's head node (stack's top node)
        popped_item = self.list.head.data
        
        # Remove list head
        self.list.remove_after(None)
        
        # Return the popped item
        return popped_item



"""
class Stack:
    # Initializes the stack. If the optional_max_length argument is omitted or 
    # negative, the stack is unbounded. If optional_max_length is non-negative, 
    # the stack is bounded.
    def __init__(self, optional_max_length = -1):
        self.stack_list = []
        self.max_length = optional_max_length
    #
    # Gets the length of the stack
    def __len__(self):
        return len(self.stack_list)
    #
    # Pops and returns the stack's top item.
    def pop(self):
        return self.stack_list.pop()
    #
    # Pushes an item, provided the push doesn't exceed bounds. Does nothing 
    # otherwise. Returns True if the push occurred, False otherwise.
    def push(self, item):
        # If at max length, return false
        if len(self.stack_list) == self.max_length:
            return False
        #
        # If unbounded, or bounded and not yet at max length, then push
        self.stack_list.append(item)
        return True
"""