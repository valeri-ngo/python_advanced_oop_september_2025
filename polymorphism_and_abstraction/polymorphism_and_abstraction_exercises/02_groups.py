class Person:

    def __init__(self, name: str, surname: str):
        self.name: str = name
        self.surname: str = surname


    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other: "Person"):
        return Person(name=self.name, surname=other.surname)

class Group:
    def __init__(self, name: str, people: list[Person]):
        self.name: str = name
        self.people: list[Person] = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other: "Group"):
        return Group(name=f'{self.name} {other.name}', people= self.people + other.people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(repr(n) for n in self.people)}"

    def __getitem__(self, index: int):
        return f"Person {index}: {self.people[index]}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)