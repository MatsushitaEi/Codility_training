# test用問題の解答
def solution(A):
    # write your code in Python 3.6
    res = 1
    A.sort()
    if(A[-1] < 0):
        return 1
    else:
        dict = {}
        for i in A:
            if i > 0:
                dict[i] = 1
        while res in dict.keys():
            res += 1
    return res
