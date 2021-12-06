class ListNode:
    def __init__(self, val, tail = None):
        self.val = val
        self.tail = tail

class Stack:
    def __init__(self):
        self.first = None
        self.length = 0

    def push(self, x):
        self.first = ListNode(x, self.first)
        self.length += 1

    def pop(self):
        if self.first == None:
            return None
        ret = self.first.val
        self.first = self.first.tail
        self.length -= 1
        return ret

    def get_length(self):
        return self.length
    
    def to_str(self):
        ret = ''
        curr = self.first
        if curr == None: return '[]'
        while True:
            ret += str(curr.val) + ' '
            if curr.tail == None:
                break
            curr = curr.tail
        return ret

    def quick_sort(self):
        array =[self.pop() for i in range(self.get_length())]
        array = self.array_quick_sort(array)
        for i in array:
            self.push(i)

    def array_quick_sort(self, array):
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            less = [i for i in array [1:] if i <= pivot]
            greater = [i for i in array[1:] if i > pivot]
            return self.array_quick_sort(less) + [pivot] + self.array_quick_sort(greater)
