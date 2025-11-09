class Equipment:
    id = 1

    def __init__(self, name: str):
        self.name: str = name
        self.id = type(self).id
        type(self).id += 1

    @classmethod
    def get_next_id(cls):
        return cls.id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"