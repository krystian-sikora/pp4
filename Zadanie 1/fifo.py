class fifo:
    def __init__(self):
        self.items = []
    def put(self,item):
        self.items.append(item)
        return None
    def pop(self):
        if len(self.items) !=0 : return self.items.pop()
        print("Can't pop from empty list")
        return None