# 1
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(X, Y, D):
    # write your code in Python 3.6
    length = Y - X
    if(length == 0):
        return 0
    result = length / D if length % D == 0 else length // D + 1
    return int(result)

# 2
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 1
    number = len(A) + 1
    sum = (number * (number + 1)) / 2
    for i in A:
        sum -= i
    return int(sum)

# 3
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    left = 0
    right = sum(A)
    result = None
    for i in range(len(A)-1):
        num = A[i]
        left += num
        right = right - num
        test = abs(left - right)
        if (result is None or test < result):
            result = test
    return result
