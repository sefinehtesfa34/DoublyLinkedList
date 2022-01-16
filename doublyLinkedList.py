**Look here this works fine**

    class Node:
        def __init__(self, data):
            self.item = data
            self.next = None
            self.prev = None
    class doublyLinkedList:
        def __init__(self):
            self.start = None
        def InsertToEmptyList(self, data):
            if self.start is None:
                new_node = Node(data)
                self.start = new_node
            else:
                print("The list is empty")
        def InsertToEnd(self, data):
            # Check if the list is empty
            if self.start is None:
                new_node = Node(data)
                self.start = new_node
                return
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            new_node = Node(data)
            temp.next = new_node
            new_node.prev = temp
        def DeleteAtStart(self):
            if self.start is None:
                print("The Linked list is empty, no element to delete")
                return 
            if self.start.next is None:
                self.start = None
                return
            self.start = self.start.next
            self.start_prev = None;
        def delete_at_end(self):
            # Check if the List is empty
            if self.start is None:
                print("The Linked list is empty, no element to delete")
                return 
            if self.start.next is None:
                self.start = None
                return
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None
        def delet_at_any(self,position):
            temp=self.start
            while position>2:
                temp=temp.next
                position-=1
            prev=temp
            temp.next=temp.next.next
            temp.prev=prev
        def Display(self):
            if self.start is None:
                print("The list is empty")
                return
            else:
                temp = self.start
                while temp is not None:
                    print("Element is: ", temp.item)
                    temp = temp.next
            print("\n")
    
    NewDoublyLinkedList = doublyLinkedList()
    NewDoublyLinkedList.InsertToEmptyList(10)
    NewDoublyLinkedList.InsertToEnd(20)
    NewDoublyLinkedList.InsertToEnd(30)
    NewDoublyLinkedList.InsertToEnd(40)
    NewDoublyLinkedList.InsertToEnd(50)
    NewDoublyLinkedList.InsertToEnd(60)
    NewDoublyLinkedList.Display()
    NewDoublyLinkedList.DeleteAtStart()
    NewDoublyLinkedList.DeleteAtStart()
    NewDoublyLinkedList.delet_at_any(3)
    NewDoublyLinkedList.Display()



