
from my_stack import Stack
from my_stack import ListNode


stack = Stack()

stack.push(5)
stack.push(7)
stack.push(10)
stack.push(1)
stack.push(4)
stack.push(8)
stack.push(6)
stack.push(16)
stack.push(14)
stack.push(41)
print('unsort: ')
print(stack.to_str())
stack.quick_sort()
print('sort: ')
print(stack.to_str())