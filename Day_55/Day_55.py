#Implement a custom iterable class.


class CustomIterable:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self  # The iterable itself is also the iterator

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration  # Signal that iteration should stop
        value = self.current
        self.current += 1
        return value

# Usage example
custom_iter = CustomIterable(1, 5)
for num in custom_iter:
    print(num)  # Output: 1, 2, 3, 4
