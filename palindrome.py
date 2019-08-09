tests = int(input())
for test in range(1, tests+1):
    word = input()
    word_r = word[::-1]
    for i in range(len(word)):
        if word[i] == word_r[i]:
            result = 1
        else:
            result = 0
    print(f'#{test} {result}')