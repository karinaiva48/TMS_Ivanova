from typing import Any
@dataclass
class DataObject:
    data: Any


class Deque:

    deque = []

    @classmethod
    def append_left(cls, obj: DataObject):
        if not isinstance(obj, DataObject):
            raise NotImplementedError
        cls.deque.insert(0, obj)
        cls.deque = [obj] + cls.deque[:]

        @classmethod
    def append_right(cls, obj: DataObject):
        if not isinstance(obj, DataObject):
            raise NotImplementedError
        cls.deque.append(obj)
        return None

    @classmethod
    def pop_left(cls):
        chunk = cls.deque[0]
        cls.deque = cls.deque[1:]
        return chunk

    @classmethod
    def pop_right(cls):
        return cls.deque.pop(len(cls.deque)-1)
        
