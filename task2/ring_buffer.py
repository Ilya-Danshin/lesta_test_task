import array


'''
Циклический буфер на основе списка
    +:
        Можно хранить объекты любого типа
    -:
        Пока не было добавлено size объектов, то есть буфер не был полностью заполнен 1 раз, 
        добавление сопровождается выделением памяти для списка, что долго
'''
class RingBufferList:
    def __init__(self, size: int):
        self.queue = []
        self.size = size
        self.cur_queue_size = 0
        self.head = 0
        self.tail = 0

    def push(self, obj):
        if self.cur_queue_size == self.head:
            self.queue.append(obj)
            self.cur_queue_size += 1
        else:
            self.queue[self.head] = obj

        self.head = (self.head + 1) % self.size
        return

    def pop(self):
        if self.cur_queue_size > self.tail:
            obj = self.queue[self.tail]
            self.tail = (self.tail + 1) % self.size
            return obj
        else:
            return None

'''
Циклический буфер на основе массива
    +:
        Операции push и pop занимают O(1)
    -:
        Можно хранить только объекты одного типа, в данной реализации int
'''
class RingBufferArray:
    def __init__(self, size: int, filler: int = 0):
        self.array = array.array('i', [filler]) * size
        self.size = size
        self.head = 0
        self.tail = 0

    def push(self, value: int):
        self.array[self.head] = value
        self.head = (self.head + 1) % self.size
        return

    def pop(self) -> int:
        value = self.array[self.tail]
        self.tail = (self.tail + 1) % self.size
        return value
