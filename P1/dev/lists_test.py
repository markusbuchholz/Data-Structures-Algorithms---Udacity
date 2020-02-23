
def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail 1")
                return
        for value in input_list:
            if head.value != value:
                print("Fail 2")
                return
            else:
                head = head.next
        print("Pass ")
    except Exception as e:
        print("Fail 3: "  + e)

##################################################



class DeepNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add_node(self, value):
        while self.next is not None:
            currnet_node = self.next
            self.next = current_node.next
        if self.next is None:
            self.next = Node(value)
            


# Test your class here

linked_list = DeepNode()
linked_list.add_node(1)
linked_list.add_node(-2)
linked_list.add_node(4)

print("Going forward through the list, should print 1, -2, 4")
node = linked_list.head
while node:
    print(node.value)
    node = node.next

print("\nGoing backward through the list, should print 4, -2, 1")
node = linked_list.tail
while node:
    print(node.value)
    node = node.previous

























def create_linked_list(input_list):
    head = None
    for value in input_list:
        if head is None:
            head = Node(value)    
        else:
        # Move to the tail (the last node)
            current_node = head
            while current_node.next:
                current_node = current_node.next
        
            current_node.next = Node(value)
    print(head)
    return head

input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list(input_list)
test_function(input_list, head)



class Node_star :
     def __init__ (self, value) :
         self.value = value
         self.next = None

    

def create_list(input_list):
    head = None
    for value in input_list:
        if head is None:
            head = Node_star(value)
        else:
            current_node = head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node_star(value)
























































