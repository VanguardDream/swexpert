import sys

sys.stdin = open("sample_input.txt",'r')

num_case = int(input())

for case in range(1, num_case +1):
    M, N = map(int,input().split())

    M_words = []
    N_words = []

    for words in range(M):
        M_words.append(str(input()))

    for words in range(N):
        N_words.append(str(input()))

    R = 0

    #Prefix compare algorithm
    for ref in M_words:
        for check in N_words:
            for idx in range(len(check)):
                if ref[idx] == check[idx]:
                    if idx == (len(check) - 1):
                        R = R + 1
                else:
                    break

    print(R)