from node import Node


class LinkedList:
    def __init__(self, head=None) -> None:
        self.__len = 0
        self.__head = None
        head != None and self.append(head)

    def append(self, *data):
        '''Adds one or more items at the end of the list.'''
        for item in data:
            if self.is_empty:
                self.__head = Node(item)
                self.__len += 1
                continue

            current = self.__head
            while current.next:
                current = current.next

            current.next = Node(item)
            self.__len += 1

        return self

# Add an item at the start of the list
    def prepend(self, *data):
        '''Adds orn or more items at the start of the list'''
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
            index = self.len - 1 if not self.is_empty else 0

        if index == 0:
            return self.delete_head()

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
        for i in range(self.len - 1):
            self.insert_at(self.len - i - 1, self.delete_head())
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

    def clear(self):
        self.__head = None
        self.__len = 0
        return self

    @property
    def head(self) -> Node | None:
        return self.__head.value if not self.is_empty else self.__head

    @property
    def tail(self) -> Node | None:
        if self.is_empty:
            return

        current = self.__head
        while current.next:
            current = current.next
        return current.value

    @property
    def len(self) -> int:
        return self.__len

    @property
    def is_empty(self) -> bool:
        return self.__len == 0

    def __str__(self) -> str:
        linked_list = ""
        current = self.__head
        while current:
            linked_list += str(current.value) + " -> "
            current = current.next

        return f'{linked_list}{current}'

    def __getitem__(self, key):
        return self.get_at(key)

    def __setitem__(self, key, value):
        return self.replace_at(key, value)

    def __iter__(self):
        current = self.__head
        while current:
            yield current.value
            current = current.next
