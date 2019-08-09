tests = int(input())
for test in range(1, tests+1):
    flys = []
    n_m = list(map(int, input().split()))
    for i in range(n_m[0]):
        flys.append(list(map(int, input().split())))
    chatch_hr = len(flys[0])-n_m[1]
    chatch_vt = len(flys)-n_m[1]
    ans = 0
    for i in range(chatch_vt):
        for j in range(n_m[1]):
            for k in range(chatch_hr):
                ans_kid += sum(flys[i+k][j:j+n_m[1]]) 
            if ans_kid >= ans:
                ans = ans_kid
    print(ans)