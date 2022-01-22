
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print('Linked list is empty')

        iterateNode = self.head
        while iterateNode:
            print(iterateNode.data, end='-->')
            iterateNode = iterateNode.next
        print('\n')

    def length(self):
        count = 0
        iterateNode = self.head
        while iterateNode:
            iterateNode = iterateNode.next
            count += 1
        return count

    def insert_at_start(self, data):
        self.head = Node(data, self.head)

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        iterateNode = self.head
        while iterateNode.next:
            iterateNode = iterateNode.next

        iterateNode.next = Node(data, None)

    def append_list(self, iterable):
        for x in iterable:
            self.append(x)

    def insert(self, index, data):
        if index < 0 or index > self.length():
            raise Exception('Index out of range')

        if index == 0:
            self.insert_at_start(data)

        count = 0
        iterateNode = self.head
        while iterateNode:
            if count == index - 1:
                iterateNode.next = Node(data, iterateNode.next)
                break

            iterateNode = iterateNode.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head == None:
            return

        iterateNode = self.head
        while iterateNode:
            if iterateNode.data == data_after:
                iterateNode.next = Node(data_to_insert, iterateNode.next)
                break
            iterateNode = iterateNode.next

    def remove(self, index):
        if index < 0 or index > self.length():
            raise Exception('Index out of range')

        if index == 0:
            self.head == self.head.next

        count = 0
        iterateNode = self.head
        while iterateNode:
            if count == index - 1:
                iterateNode.next = iterateNode.next.next
                break
            iterateNode = iterateNode.next
            count += 1

    def remove_by_value(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        iterateNode = self.head
        while iterateNode.next:
            if iterateNode.next.data == value:
                iterateNode.next = iterateNode.next.next
                break

            iterateNode = iterateNode.next

    def pop(self):
        if self.head is None or self.head.next is None:
            return

        iterateNode = self.head
        while iterateNode.next.next:
            iterateNode = iterateNode.next

        iterateNode.next = None


if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.append('vaibhav')
    linked_list.insert_at_start('vinod')
    linked_list.append('anubhav')
    linked_list.append('anubhav2')
    linked_list.append('anubhav3')
    linked_list.insert(3, 'meera')

    linked_list.print()
    linked_list.insert_after_value('vinod', 'anubhav4')
    linked_list.print()

    linked_list.remove_by_value('vinod')
    linked_list.print()

    linked_list.remove(2)
    linked_list.print()

    linked_list.pop()
    linked_list.print()

    print(linked_list.length())
