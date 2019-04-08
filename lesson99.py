# 99-4
def solution(A):
    # write your code in Python 3.6
    sum = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] < A[i]:
                sum += 1
    return sum


# 99-5
# 答え間違ってるので改善が必要
def solution(A):
    # write your code in Python 3.6
    Y = [i.y for i in A]
    X = [i.y for i in A]
    ite_max_y = Y.index(max(Y))
    ite_max_x = X.index(max(X))
    ite_min_y = Y.index(min(Y))
    ite_min_x = X.index(min(X))

    # yの最大値を始点としてcosinが最大となる点を探す
    comp = False
    ite = ite_max_y
    tyouten = {}
    tyouten[ite] = 1
    while comp == False:
        plus_a = 0
        minus_a = 0
        plus_ite = ite
        minus_ite = ite
        for i in range(len(A)):
            if i == ite:
                next
            # 傾き
            if A[ite].x - A[i].x != 0 and A[ite].y - A[i].y != 0:
                test_a = (A[ite].y - A[i].y) / (A[ite].x - A[i].x)
                if test_a == plus_a:
                    tyouten[i] = 1
                elif test_a == minus_a:
                    tyouten[i] = 1

                if test_a > 0 and (plus_ite == ite or plus_a > test_a):
                    plus_a = test_a
                    plus_ite = i
                elif test_a < 0 and (minus_ite == ite or minus_a < test_a):
                    minus_a = test_a
                    minus_ite = i
        if plus_ite in tyouten.keys() and minus_ite in tyouten.keys():
            comp = True
        else:
            if plus_ite not in tyouten.keys():
                ite = plus_ite
            else:
                ite = minus_ite
            tyouten[plus_ite] = 1
            tyouten[minus_ite] = 1

    if len(A) == len(tyouten):
        return -1

    for i in tyouten.keys():
        if i+1 not in tyouten.keys():
            return i+1
