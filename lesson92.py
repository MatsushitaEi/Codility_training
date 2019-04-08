# 2
def solution(K, C, D):
    # write your code in Python 3.6
    clean = {}
    dirty = {}
    total = 0
    for i in C:
        clean[i] = clean.get(i, 0) + 1
        if clean[i] % 2 == 0:
            total += clean[i] // 2
            del clean[i]

    for i in D:
        dirty[i] = dirty.get(i, 0) + 1

    time = 1
    if K > 0:
        for j in C:
            if j in clean.keys() and j in dirty.keys():
                total += 1
                del clean[j]
                dirty[j] -= 1
                if dirty[j] == 0:
                    del dirty[j]
                if time == K:
                    break
                else:
                    time += 1

    if K - time >= 1:
        time += 1
        for j in D:
            if j in dirty.keys() and dirty[j] > 1:
                total += 1
                dirty[j] -= 2
                if dirty[j] == 0:
                    del dirty[j]
                if time == K:
                    break
                elif time > K:
                    total -= 1
                    break
                else:
                    time += 2
    return total
