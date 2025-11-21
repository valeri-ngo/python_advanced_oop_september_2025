def read_next(*collections):
    for seq in collections:
        # yield from seq
        for item in seq:
            yield item


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
print()
for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)