# 5-2
def solution(S, P, Q):
    # write your code in Python 3.6
    res = []
    for i in range(len(P)):
        start = P[i]
        end = Q[i] + 1
        sch = S[start:end]
        if sch.find("A") != -1:
            res.append(1)
        elif sch.find("C") != -1:
            res.append(2)
        elif sch.find("G") != -1:
            res.append(3)
        else:
            res.append(4)

    return res
