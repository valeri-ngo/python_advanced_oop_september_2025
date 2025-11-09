class Trainer:

    id = 1

    def __init__(self, name: str):
        self.name: str = name
        self.id = type(self).id
        type(self).id += 1

    @staticmethod
    def get_next_id():
        return Trainer.id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"