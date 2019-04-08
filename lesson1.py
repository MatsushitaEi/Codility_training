def solution(N):
    # write your code in Python 3.6
    res = []
    i = N
    bin = 0
    if i < 5:
        return 0
    while i >= 1:
        bin = i % 2
        i = i // 2
        res.insert(0, bin)
    return(calc(res))


def calc(res):
    count = 0
    find = 0
    find_flg = 0
    for i in res:
        if (i == 1):
            if(find_flg == 1):
                if(count < find):
                    count = find
            find_flg = 1
            find = 0
        else:
            if(find_flg == 1):
                find += 1
    return count
