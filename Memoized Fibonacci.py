class Memoize:
    def __init__(self, fibonacci):
        self.fibonacci = fibonacci
        self.memoria = {}

    def __call__(self, *args):
        if args not in self.memoria:
            self.memoria[args] = self.fibonacci(*args)
        return self.memoria[args]

@Memoize
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(200))