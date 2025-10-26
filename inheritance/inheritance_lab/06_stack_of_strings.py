class Stack:
    def __init__(self, *args):
        self.data: list = []

        for el in args:
            if isinstance(el, str):
                self.data.append(el)

    def push(self, element):
        if isinstance(element, str):
            self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        result = reversed(self.data)
        return f"[{', '.join(result)}]"

