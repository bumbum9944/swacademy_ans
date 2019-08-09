# 수도쿠 검증 : 3개줄을 3개씩 검사하고 다음 시작점+3번째 줄로 넘어감
# 가로 세로 모두 3칸!
def sudoku_check(puzzle):
    sudoku_list = puzzle
    sudoku_col = list(zip(*sudoku_list))
    for sudoku in sudoku_list:
        numbers = list(range(1,10))
        for num in sudoku:
            if num in numbers:
                numbers.remove(num)
        if len(numbers):
            return f'#{test} 0'
    for sudoku in sudoku_col:
        numbers = list(range(1,10))
        for num in sudoku:
            if num in numbers:
                numbers.remove(num)
        if len(numbers):
            return f'#{test} 0'
    check = list(range(0,9,3))
    for i in check:
        # 한줄씩
        check2 = list(range(0,9,3))
        for j in check2:
            nums = list(range(1,10))
            for ver in sudoku_list[j:j+3]:
            # 각 줄의 3개만 확인!
                for hor in ver[i:i+3]:
                    if hor in nums:
                        nums.remove(hor)
            if len(nums):
                return f'#{test} 0'
    else:
        return f'#{test} 1'

tests = int(input())
for test in range(1,tests+1):
    sudoku_list = []
    for i in range(9):
        sudoku = list(map(int, input().split()))
        sudoku_list.append(sudoku)
    print(sudoku_check(sudoku_list))