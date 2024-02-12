class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
        
    def isEmpty(self):
        if self.size() == 0:
            return True
        return False

    def push(self, item):
        if self.full() == False:
            self.items.append(item)
        else: return False
        
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else: return None
    
    def size(self):
        return len(self.items)

    def full(self):
        if self.size() >= self.limit:
            return True
        return False

    def search(self, target):
        position = self.size() - 1
        for element in self.items:
            if target == element:
                return position
            else:
                position = position - 1
        return -1
