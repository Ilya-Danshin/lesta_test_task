

class IsEven:
    '''
    +:
        Простая реализация
        Работает для любых типов чисел
        Сложность О(1)
    '''
    @staticmethod
    def isEvenBasic(value):
        return value % 2 == 0

    '''
    +:
        Сложность О(1)
    -:
        Не работает для чисел с плавающей запятой (float)
    '''
    @staticmethod
    def isEvenByBit(value: int):
        return value & 0b1 == 0

    '''
    +:
        Работает для любых типов чисел
    -:
        Сложность O(n/2) (Из числа придётся вычитать 2 n/2 раз)
    '''
    @staticmethod
    def isEvenBySubtraction(value):
        while not (value == 0 or value == 1):
            value -= 2

        return value == 0
