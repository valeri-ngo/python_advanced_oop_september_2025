def count_calls(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        func(*args, **kwargs)
        print(f'Printed {count} times')
    return wrapper


@count_calls
def add(a, b):
    return a + b

add(1, 2)
add(5, 7)
add(0, 0)
# Function add was called 3 times
