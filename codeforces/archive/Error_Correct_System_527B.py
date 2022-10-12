# Time: Jul/19/2022 21:14
# Title: B - Error Correct System
# Submission ID: 164931096
# Language: Python


def main():
    l = int(input())
    a = input()
    b = input()
    ad = {}
    bd = {}
    rd = []
    for i in range(l):
        if a[i] != b[i]:
            rd.append(i)
            if a[i] in ad:
                ad[a[i]].add(i)
            else:
                ad[a[i]] = {i}
            if b[i] in bd:
                bd[b[i]].add(i)
            else:
                bd[b[i]] = {i}
    one_time = None
    for i in rd:
        if a[i] not in bd and b[i] not in ad:
            continue
        if a[i] not in bd:
            if not one_time:
                one_time = i, list(ad[b[i]])[0]
        elif b[i] not in ad:
            if not one_time:
                one_time = i, list(bd[a[i]])[0]
        else:
            pos = ad[b[i]].intersection(bd[a[i]])
            if pos:
                print(len(rd) - 2)
                print(i + 1, list(pos)[0] + 1)
                return
            elif not one_time:
                one_time = i, list(bd[a[i]])[0]
    if not one_time:
        print(len(rd))
        print (-1, -1)
    else:
        print (len(rd) - 1)
        print (one_time[0] + 1, one_time[1] + 1)


if __name__ == '__main__':
    main()
