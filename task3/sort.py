
'''

'''
class MergeSort:
    @staticmethod
    def run(elems: list, reverse: bool = False):
        if reverse:
            res = MergeSort.sort_reverse(elems)
        else:
            res = MergeSort.sort(elems)

        return res

    @staticmethod
    def sort(elems: list) -> list:
        if len(elems) == 1:
            return elems
        if len(elems) == 2:
            if elems[0] > elems[1]:
                elems[0], elems[1] = elems[1], elems[0]

            return elems

        e1 = MergeSort.sort(elems[0:len(elems)//2])
        e2 = MergeSort.sort(elems[len(elems)//2:])

        elems = MergeSort.merge(e1, e2)

        return elems

    @staticmethod
    def merge(e1: list, e2: list) -> list:
        i, j = 0, 0

        res = []

        while i < len(e1) and j < len(e2):
            if e1[i] < e2[j]:
                res.append(e1[i])
                i += 1
            else:
                res.append(e2[j])
                j += 1

        while i < len(e1):
            res.append(e1[i])
            i += 1

        while j < len(e2):
            res.append(e2[j])
            j += 1

        return res

    @staticmethod
    def sort_reverse(elems: list) -> list:
        if len(elems) == 1:
            return elems
        if len(elems) == 2:
            if elems[0] < elems[1]:
                elems[0], elems[1] = elems[1], elems[0]

            return elems

        e1 = MergeSort.sort_reverse(elems[0:len(elems)//2])
        e2 = MergeSort.sort_reverse(elems[len(elems)//2:])

        elems = MergeSort.merge_reverse(e1, e2)

        return elems

    @staticmethod
    def merge_reverse(e1: list, e2: list) -> list:
        i, j = 0, 0

        res = []

        while i < len(e1) and j < len(e2):
            if e1[i] > e2[j]:
                res.append(e1[i])
                i += 1
            else:
                res.append(e2[j])
                j += 1

        while i < len(e1):
            res.append(e1[i])
            i += 1

        while j < len(e2):
            res.append(e2[j])
            j += 1

        return res
