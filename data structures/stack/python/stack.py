
class Stack:
    def __init__(self, *items) -> None:
        self.__items = {}
        self.__len = 0
        self.push(*items)

    def push(self, *items):
        '''adds one or more items to the stack'''
        for item in items:
            self.__items.update({self.__len: item})
            self.__len += 1
        return self

    def pop(self):
        '''removes and returns the item on top of the stack. If the stack is empty, it returns None'''
        if self.is_empty:
            return

        self.__len -= 1
        return self.__items.pop(self.__len)

    def has_item(self, item) -> bool:
        '''checks whether a value is present in the stack'''
        return list(self.__items.values()).count(item) != 0

    def map(self, func):
        '''transforms each item in the stack based on the conditions provided by func'''
        for key in self.__items:
            self.__items[key] = func(self.__items[key])
        return self

    def all(self, func) -> bool:
        for item in self:
            if not func(item):
                return False

        return True

    def any(self, func) -> bool:
        for item in self:
            if func(item):
                return True
        return False

    def clear(self):
        '''removes all the items in the stack'''
        self.__items.clear()
        self.__len = 0
        return self

    @property
    def is_empty(self) -> bool:
        return self.__len == 0

    @property
    def len(self) -> int:
        return self.__len

    @property
    def peek(self):
        return self.__items[self.__len - 1]

    # Let's make the stack iterable. This is useful when looping through the values in the stack using the for-in loop

    def __iter__(self):
        for key in self.__items:
            yield self.__items[key]

    # The string representation of the stack should simply be a list of the values on the stack.
    def __str__(self) -> str:
        return f'{list(self.__items.values())}'
