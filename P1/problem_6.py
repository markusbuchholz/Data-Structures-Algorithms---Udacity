class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    
    linked_union = LinkedList()
    current_element1 = llist_1.head
    current_element2 = llist_2.head
    temp_union_list = []

    while current_element1 is not None:
        temp_union_list.append(current_element1.value)
        current_element1 = current_element1.next
    while current_element2 is not None:
        temp_union_list.append(current_element2.value)
        current_element2 = current_element2.next
    
    temp_union_list_set = set(temp_union_list)
    for set_el in temp_union_list_set:
        linked_union.append(set_el)
    return linked_union

def intersection(llist_1, llist_2):
    linked_intersection = LinkedList()

    current_element1 = llist_1.head
    current_element2 = llist_2.head

    temp_inter_list1 = []
    temp_inter_list2 = []
    temp_inter_list3 = []
    temp_inter_list4 = []

    while current_element1 is not None:
        temp_inter_list1.append(current_element1.value)
        current_element1 = current_element1.next

    while current_element2 is not None:
        temp_inter_list2.append(current_element2.value)
        current_element2 = current_element2.next
    
    temp_inter_list3 = temp_inter_list1 + temp_inter_list2

    for k in range(len(temp_inter_list1)):
        if temp_inter_list3[k] in temp_inter_list2:
            temp_inter_list4.append(temp_inter_list1[k])
    
    set_list = set (temp_inter_list4)
    for set_el in set_list:
        linked_intersection.append(set_el)
    return linked_intersection



if __name__ == '__main__':

    def test_1():
        print("***************************************")
        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()

        element_1 = [3,2,4,35,6,65,6,4,3,21]
        element_2 = [6,32,4,9,6,1,11,21,1]

        for i in element_1:
            linked_list_1.append(i)

        for i in element_2:
            linked_list_2.append(i)

        #print (union(linked_list_1,linked_list_2))
        #print (intersection(linked_list_1,linked_list_2))
        #test prints -----------
        #32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 
        #4 -> 21 -> 6 -> 


    def test_2():
        print("***************************************")

        linked_list_3 = LinkedList()
        linked_list_4 = LinkedList()

        element_1 = [3,2,4,35,6,65,6,4,3,23]
        element_2 = [1,7,8,9,11,21,1]

        for i in element_1:
            linked_list_3.append(i)

        for i in element_2:
            linked_list_4.append(i)

        #print (union(linked_list_3,linked_list_4))
        #print (intersection(linked_list_3,linked_list_4))
        #test prints -----------
        #65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 

    def test_3():
        print("***************************************")

        linked_list_5 = LinkedList()
        linked_list_6 = LinkedList()

        element_1 = [3,2,4,'bb',35,6,65,6,4,'aa',3,23]
        element_2 = [1,7,8,9,11,35,6,65,'aa',26,21]

        for i in element_1:
            linked_list_5.append(i)

        for i in element_2:
            linked_list_6.append(i)

        #print (union(linked_list_5,linked_list_6))
        #print (intersection(linked_list_5,linked_list_6))
        #test prints -----------
        #aa -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> bb -> 21 -> 23 -> 26 -> 
        #aa -> 65 -> 35 -> 6 -> 

    def test_4():
        print("***************************************")

        linked_list_7 = LinkedList()
        linked_list_8 = LinkedList()

        element_1 = [3,2,4,'bb',35,6,65,6,4,'aa',3,23]
        element_2 = ['',None, True]

        for i in element_1:
            linked_list_7.append(i)

        for i in element_2:
            linked_list_7.append(i)

        #print (union(linked_list_7,linked_list_8))
        #print (intersection(linked_list_7,linked_list_8))
        #test prints -----------
        #aa -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 ->  -> True -> bb -> 23 -> None -> 





    test_1()
    test_2()
    test_3()
    test_4()