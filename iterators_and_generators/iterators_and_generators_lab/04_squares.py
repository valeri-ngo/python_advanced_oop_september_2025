def squares(end):
    num = 1
    while num <= end:
        yield num * num
        num += 1


print(list(squares(5)))