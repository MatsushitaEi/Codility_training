# 2
def solution(A):
    # write your code in Python 3.6
    length = len(A)
    if length < 2:
        result = 0 if length == 0 else abs(A[0])
        return result
    # 配列の各値の絶対値を取り、それを降順ソート
    abs_arr = [abs(i) for i in A]
    half_max = sum(abs_arr) // 2
    is_exist = [0] * (sum(abs_arr) + 1)
    is_exist[0] = 1

    for i in abs_arr:
        sch = len(is_exist) - 1
        while sch >= 0:
            if (is_exist[sch] == 1):
                is_exist[sch+i] = 1
            sch -= 1

    for i in range(half_max, len(is_exist)):
        if(is_exist[i] == 1):
            return abs(sum(abs_arr) - i * 2)
