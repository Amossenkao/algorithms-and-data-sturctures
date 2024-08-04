from node import Node


class LinkedList:
    def __init__(self, head=None) -> None:
        self.__len = 0
        self.__head = None
        self.__tail = None
        if head is not None:
            self.append(head)

    def append(self, *data):
        '''Adds one or more items at the end of the list.'''
        for item in data:
            if self.is_empty:
                self.__head = Node(item)
                self.__tail = self.__head
            else:
                self.__tail.next = Node(item)
                self.__tail = self.__tail.next
            self.__len += 1
        return self

    def prepend(self, *data):
        '''Adds one or more items at the start of the list'''
        for item in data:
            self.__head = Node(item, self.__head)
            self.__len += 1

        return self

    def delete_head(self):
        '''Deletes and returns the head of the list'''
        if self.is_empty:
            return
        data = self.__head.value
        self.__head = self.__head.next
        self.__len -= 1
        return data

    def delete_tail(self):
        '''Deletes and returns the last item in the list'''
        if self.is_empty:
            return

        if self.len == 1:
            data = self.__head.value
            self.__head = None
            self.__len -= 1
            return data

        previous = self.__head
        current = previous.next
        while current.next:
            current = current.next
            previous = previous.next

        data = current.value
        previous.next = None
        self.__tail = previous
        self.__len -= 1
        return data

    def get_at(self, index: int):
        if self.is_empty:
            return

        if not isinstance(index, int) or index < 0:
            raise ValueError('index must be a non-negative integer')

        if index > self.__len - 1:
            raise IndexError('Index out of range')

        current_index = 0
        current = self.__head
        while current:
            if current_index == index:
                return current.value
            current = current.next
            current_index += 1

    def insert_at(self, index: int, data):
        '''Inserts an item at a specified index'''
        if not isinstance(index, int) or index < 0:
            raise ValueError('index must be a non-negative integer')

        if index > self.__len:
            index = self.__len

        if index == 0:
            return self.prepend(data)
        elif index == self.__len:
            return self.append(data)

        current_index = 0
        current = self.__head
        while current:
            if current_index == index - 1:
                current.next = Node(data, current.next)
                self.__len += 1
                return self

            current = current.next
            current_index += 1

    def delete_at(self, index: int):
        '''Replaces the item at the specified index. If no replacement is provided, the item at the index is simply deleted.'''
        if not isinstance(index, int) or index < 0:
            raise ValueError('index must be a non-negative integer')

        if self.is_empty:
            return

        if index > self.len - 1:
            index = self.len - 1

        if index == 0:
            return self.delete_head()
        elif index == self.__len - 1:
            return self.delete_tail()

        current_index = 0
        previous = self.__head
        current = previous.next
        while current:
            if current_index == index - 1:
                data = current.value
                previous.next = current.next
                self.__len -= 1
                return data

            previous = previous.next
            current = current.next
            current_index += 1

    def replace_at(self, index: int, replacement):
        if not isinstance(index, int) or index < 0:
            raise ValueError('index must be a non-negative integer')
        if self.is_empty:
            return

        if index > self.__len - 1:
            index = self.__len - 1

        current_index = 0
        current = self.__head
        while current:
            if current_index == index:
                current.value = replacement
                return self
            current = current.next
            current_index += 1

    def has_item(self, item) -> bool:
        current = self.__head
        while current:
            if current.value == item:
                return True
            current = current.next
        return False

    def reverse(self):
        prev = None
        current = self.__head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.__head = prev
        return self

    def count(self, item) -> int:
        count = 0
        for value in self:
            if value == item:
                count += 1
        return count

    def map(self, func):
        current = self.__head
        while current:
            current.value = func(current.value)
            current = current.next
        return self

    def filter(self, func):
        index = 0
        while index < self.__len:
            item = self.get_at(index)
            if not func(item):
                self.delete_at(index)
                continue
            index += 1
        return self

    def any(self, func):
        for value in self:
            if func(value):
                return True

        return False

    def all(self, func):

        for value in self:
            if not func(value):
                return False
        return True

    def sort(self, reverse=False):
        """Sorts the linked list in place. If `reverse` is True, the list is sorted in descending order. This function implements a `bubble sort`, which is ineffecient for large number of inputs"""

        if self.__len < 2:
            return self

        sorted_nodes = 1
        while sorted_nodes < self.__len:

            current = self.__head
            next_node = current.next
            index = 0
            while index < self.__len - sorted_nodes:
                a, b = current.value, next_node.value

                if (reverse and a < b) or (not reverse and a > b):
                    current.value = b
                    next_node.value = a

                current = next_node
                next_node = current.next
                index += 1
            sorted_nodes += 1
        return self

    def clear(self):
        self.__head = None
        self.__tail = None
        self.__len = 0
        return self

    @property
    def head(self):
        return self.__head.value if not self.is_empty else self.__head

    @property
    def tail(self):
        if self.is_empty:
            return
        return self.__tail

    @property
    def len(self) -> int:
        return self.__len

    @property
    def is_empty(self) -> bool:
        return self.__len == 0

    def __str__(self) -> str:
        return " -> ".join(map(str, self)) + " -> None"

    def __getitem__(self, key):
        return self.get_at(key)

    def __setitem__(self, key, value):
        return self.replace_at(key, value)

    def __iter__(self):
        current = self.__head
        while current:
            yield current.value
            current = current.next
