class Queue:

    def __init__(self):
        self.queue = []
    
    def __str__(self):
        return str(self.queue)

    def pop(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def push(self, item):
        self.queue.append(item)

    def is_empty(self):
        return len(self.queue) == 0
    
kolejka = Queue()

kolejka.push(5)
print(kolejka)
kolejka.push(3)
print(kolejka)
kolejka.push(7)
print(kolejka)
kolejka.push(9)
print(kolejka)
kolejka.push(2)
print(kolejka)

for j in range(3):
    kolejka.pop()
    print(kolejka)
