class Stack:
    def __init__(self, data: str):
        self.data = [data]

    def push(self, element):
        self.data.append(element)

    def pop(self):
        last_el = self.data[-1]
        self.data.pop()
        return last_el

    def top(self):
        return self.data[0]

    def is_empty(self):
        if len(self.data) > 0:
            return False
        return True

    def __str__(self):
        return "[" + ", ".join(reversed(self.data)) + "]"
