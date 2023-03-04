class fifo:
    items = []
    def put(self,item):
        self.items.append(item)
        return None
    def pop(self):
        return self.items.pop()