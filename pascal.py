tests = int(input())
for test in range(1,tests+1):
    num = int(input())
    print(f'#{test}')
    numbers = range(1,num+1)
    num_list = []
    for number in numbers:
        if number == 1:
            num_list = [1]
        elif number == 2:
            num_list = [1, 1]
        else:
            i = 1
            for nu in num_list[:len(num_list)-1]:
                num_list[i] = nu + num_list[i]
                i += 1
            num_list.append(1)
        for nu in num_list:
            print(f'{nu} ', end='')
        print()