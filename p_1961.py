tests = int(input())
for test in range(1, tests+1):
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))


def rotation(matrix):
    matrix_col90 = list(zip(*matrix))
    matrix_col180 = list(zip(*matrix))
    matrix_col270 = list(zip(*matrix))

        
def prin(matrix_90, matrix_180, matrix_270):
    N = len(rot_matrix)
    for i in range(N):
        m90 = 