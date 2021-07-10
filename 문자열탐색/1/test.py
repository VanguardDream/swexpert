from os import rename
import sys

sys.stdin = open("sample_input.txt",'r')

test_case = int(input())

for case in range(1, test_case + 1):
    # get M, N
    # MN = str(input()).split()
    # M = int(MN[0])
    # N = int(MN[1])
    M, N = map(int, input().split())
    
    M_words = []
    for words in range(M):
        M_words.append(str(input()))

    N_words = []
    for words in range(N):
        N_words.append(str(input()))

    R = 0

    if M > N:
        for ref in N_words:
            for check in M_words:
                if ref == check:
                    R = R + 1
                else:
                    continue
    else:
        for ref in M_words:
            for check in N_words:
                if ref == check:
                    R = R + 1
                else:
                    continue

    print('#'+str(case)+' '+str(R))