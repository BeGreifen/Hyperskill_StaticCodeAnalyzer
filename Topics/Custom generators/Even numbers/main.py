def even():
    num = 0
    while True:
        yield num
        num += 2


def print_first_n_even_numbers(n):
    even_gen = even()
    for _ in range(n):
        print(next(even_gen))


# Example usage:
n = int(input())
print_first_n_even_numbers(n)