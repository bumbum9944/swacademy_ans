tests = int(input())
for test in range(1, tests+1):
    num = int(input())
    total = 0
    for i in range(1, num+1):
        if i % 2:
            total += i
        else:
            total -= i
    print(f'#{test} {total}')