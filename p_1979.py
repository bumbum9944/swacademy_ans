tests = int(input())
for test in range(1, tests+1):
    nums = list(map(int, input().split()))
    N = nums[0]
    k = nums[1]
    puzzle = []
    for i in range(N):
        puzzle.append(list(map(int, input().split())))
# 가로확인
    ans = 0
    for ver in puzzle:
        check_big = []
        check = []
        for i, hor in enumerate(ver):
            if hor:
                if hor not in check:
                    check.append(hor)
                else:
                    if ver[i-1]:
                        check.append(hor)
            else:
                check_big.append(check)
                check=[]
        else:
            check_big.append(check)
        for checking in check_big:
            if len(checking) == k:
                ans += 1
# 세로확인
    for i in range(N):
        check_big = []
        check = []
        for j, ver in enumerate(puzzle):
            if ver[i]:
                if ver[i] not in check:
                    check.append(ver[i])
                else:
                    if puzzle[j-1]:
                        check.append(hor)
            else:
                check_big.append(check)
                check=[]
        else:
            check_big.append(check)
        for checking in check_big:
            if len(checking) == k:
                ans += 1
    print(f'#{test} {ans}')