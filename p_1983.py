tests = int(input())
# 성적 리스트
grades = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']
for test in range(1, tests+1):
    target = list(map(int,input().split()))
    step = target[0] // 10
    target_p = str(target[1])
    stus = []
    for i in range(target[0]):
        stus.append(sum(list(map(int, input().split()))))
    # 총점을 정렬해 주어야한다.
    stus_fin = sorted(stus)
    # D0부터 N/10명씩 묶어주자!
    ans = {}
    index = 0
    count = 0
    for stu in stus_fin:
        count += 1
        ans[str(stus_fin.index(stu))] = grades[index]
        if count == step:
            count = 0
            index += 1
    print(f'#{test} {ans[target_p]}')