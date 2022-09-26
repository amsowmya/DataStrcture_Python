'''
def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node

def remove_by_value(self, data):
    # Remove first node that contains data
'''

class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self, data):
        self.head = Node(data, self.head)

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+ '-->'
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, self.head)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_value(self, datalist):
        self.head = None
        for data in datalist:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index<0 or index>=self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    # Problem 1
    def insert_after_value(self, data_after, data_to_insert):
        count = 0
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                return

            itr = itr.next
            count += 1

    # Problem 1
    def remove_by_value(self, data):

        index = 0
        itr = self.head
        while itr:
            if itr.data == data:
                self.remove_at(index)

            itr = itr.next
            index += 1

        # itr = self.head
        # count = 0
        # while itr:
        #     if count == index - 1:
        #         itr.next = itr.next.next
        #         break
        #
        #     itr = itr.next
        #     count += 1


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_value(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.print()
    ll.remove_by_value("grapes")
    ll.print()

    # ll = LinkedList()
    # ll.insert_value([2, 4, 6, 8])
    # ll.print()
    # ll.insert_value(["banana","mango","grapes","orange"])
    # ll.print()
    # ll.insert_at_beginning(3)
    # ll.insert_at_beginning(8)
    # ll.insert_at_beginning(9)
    # ll.insert_at_beginning(10)
    # ll.print()
    # ll.insert_at_end(4)
    # ll.insert_at(0, 'b')
    # ll.remove_at(0)
    # ll.insert_after_value(9, 10)
    # ll.remove_by_value(4)
    # ll.print()