
class Queue:
    def __init__(self, *items) -> None:
        self.__items = {}
        self.__len = 0
        self.__head = 0
        self.__tail = 0
        self.enqueue(*items)

    def enqueue(self, *items):
        for item in items:
            self.__items[self.__tail] = item
            self.__tail += 1
            self.__len += 1
        return self

    def dequeue(self):
        if self.is_empty:
            return

        removed_item = self.__items.pop(self.__head)
        self.__head += 1
        self.__len -= 1
        return removed_item

    def has_item(self, item) -> bool:
        return list(self.__items.values()).count(item) != 0

    def map(self, func):
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
        self.__items.clear()
        self.__len = 0
        self.__head = 0
        self.__tail = 0
        return self

    @property
    def is_empty(self) -> bool:
        return self.__len == 0

    @property
    def len(self) -> int:
        return self.__len

    def __iter__(self):
        for key in self.__items:
            yield self.__items[key]

    def __str__(self) -> str:
        return f'{list(self.__items.values())}'