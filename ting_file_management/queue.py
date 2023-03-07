from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = list()
        self.head = None
        self.tail = None
        self.__length = 0

    def __len__(self):
        return self.__length

    def enqueue(self, value):
        self._data.append(value)
        if len(self._data) == 0:
            self.head = value
            self.tail = value
        self.__length += 1

    def dequeue(self):
        if len(self._data) == 0:
            self.head = None
            self.tail = None
        self.head = self._data[1]
        self.__length -= 1
        return self._data.pop(0)

    def search(self, index):
        if not 0 <= index < len(self):
            raise IndexError
        return self._data[index]
