# class Stack:
#     def __init__(self):
#         self.stack = []
#     def push(self,data):
#         if len(self.stack)<5:
#             self.stack.append(data)
#         else:
#             print("Overflow")
#     def pop(self):
#         if len(self.stack) == 0:
#             print("Stack underflow")
#             return
#         else:
#             self.stack.pop()
#     def isEmpty(self):
#         return len(self.stack) == 0
#     def peek(self):
#         print(self.stack[-1])
#     def display(self):
#         print(self.stack)
# s = Stack()
# s.push(7)
# s.push(10)
# s.push(17)
# s.push(32)
# s.push(49)
# s.push(55)


def valid_p(s):
    stack=[]
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if not stack:
                return False
            top=stack.pop()
            if(ch == ")" and top!= "(") or (ch == "}" and top != "["):
                return False
    return len(stack)==0
print(valid_p("[[()]}"))
