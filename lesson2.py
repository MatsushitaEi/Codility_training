# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# 2-1


def solution(A, K):
    # write your code in Python 3.6
    if(len(A) != 0):
        for i in range(K):
            last = A.pop(-1)
            A.insert(0, last)
    return(A)


# 2-2
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    sum = {}
    for i in A:
        if(i in sum):
            sum[i] += 1
        else:
            sum[i] = 1
    for key in sum:
        if (sum[key] % 2 == 1):
            return key
