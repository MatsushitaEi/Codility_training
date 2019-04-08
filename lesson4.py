# 1
def solution(A):
    # write your code in Python 3.6
    number = len(A)
    expect = (number * (number + 1)) / 2
    test = sum(A)

    result = 1 if (expect == test) else 0

    if (result == 1):
        dict = {}
        for i in A:
            if (i > number or i in dict):
                result = 0
                break
            dict[i] = 1
    return result


# 2
def solution(X, A):
    # write your code in Python 3.6
    dict = {}
    res = 0
    expect = (X * (X + 1)) / 2
    time = 0
    for i in A:
        if (i < X + 1 and i not in dict):
            res += i
            dict[i] = 1
            if(expect == res):
                return time
        time += 1
    return -1


# 3
def solution(N, A):
    # write your code in Python 3.6
    array = [0] * N
    max = 0
    for i in A:
        if(i == N + 1):
            array = [max] * N
        else:
            array[i-1] += 1
            if(max < array[i-1]):
                max = array[i-1]
    return array


# 4
def solution(A):
    # write your code in Python 3.6
    result = 1
    arr = []
    dict = {}
    for i in A:
        if i > 0 and i not in dict:
            arr.append(i)
            dict[i] = 1
    arr.sort()
    for i in arr:
        if i != result:
            return result
        result += 1
    return result
