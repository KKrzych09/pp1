class Stack:

    def __init__(self):
        self.stack = []
    
    def __str__(self):
        return str(self.stack)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack) == 0
    
stos = Stack()

stos.push(5)
print(stos)
stos.push(3)
print(stos)
stos.push(7)
print(stos)
stos.push(9)
print(stos)
stos.push(2)
print(stos)

for j in range(3):
    stos.pop()
    print(stos)
