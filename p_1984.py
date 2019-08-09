tests = int(input())
for test in range(1, tests+1):
    numbers = list(map(int, input().split()))
    num_max = max(numbers)
    num_min = min(numbers)
    numbers.remove(num_max)
    numbers.remove(num_min)
    result = round(sum(numbers) / len(numbers))
    print('#{0} {1}'.format(test, result))