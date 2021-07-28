def decorator(num):
    def fun(numbers):
        num(['+91 ' + i[-10:-5] + ' '  + i[-5:] for i in numbers])
    return fun

@decorator
def sort_numbers(numbers):
    print(*sorted(numbers), sep='\n')

if __name__ == '__main__':
    n = int(input())
    numbers = [input(f"number_{i+1} = ") for i in range(n)]
    sort_numbers(numbers)