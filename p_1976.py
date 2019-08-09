tests = int(input())

for test in range(1,tests+1):
    times = list(map(int, input().split()))
    hour = 0
    minute = 0
    for i in range(len(times)):
        if not i % 2:
            hour += times[i]
            if hour >= 13:
                hour -= 12 
        else:
            minute += times[i]
            if minute >= 60:
                minute -= 60
                hour += 1
    print(f'#{test} {hour} {minute}')