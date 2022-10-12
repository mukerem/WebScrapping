# Time: Jul/14/2022 21:35
# Title: D - Name That Tune
# Submission ID: 164181142
# Language: Python


def main():
    n, time = map(int, input().split())
    pp, qq, tt, qqtt = [], [], [], []
    for i in range(n):
        a, b = input().split()
        p = float(a) / 100.
        pp.append(p)
        q = 1. - p
        qq.append(q)
        t = int(b) - 1
        tt.append(t)
        qqtt.append(q ** t)
    t_cur, u_cur, t_prev, u_prev = ([0.] * (time + 1) for _ in '1234')
    for k in range(n - 1, 0, -1):
        q_1, t_1, qt_1 = qq[k - 1], tt[k - 1], qqtt[k - 1]
        p, t, qt = pp[k], tt[k], qqtt[k]
        q = w = qq[k]
        for i in range(time):
            t_cur[i + 1] = x = ((p * u_prev[i] + 1. - w) if i < t else
                                (p * u_prev[i] + qt * t_prev[i - t] + 1.))
            u_cur[i + 1] = ((q_1 * u_cur[i] + x) if i + 1 < t_1 else
                            (q_1 * u_cur[i] + x - qt_1 * t_cur[i - t_1 + 1]))
            w *= q
        t_cur, u_cur, t_prev, u_prev = t_prev, u_prev, t_cur, u_cur
        t_cur[0] = u_cur[0] = 0.
    p, t, qt = pp[0], tt[0], qqtt[0]
    q = w = qq[0]
    for i in range(t):
        t_cur[i + 1] = p * u_prev[i] + 1. - w
        w *= q
    for i in range(t, time):
        t_cur[i + 1] = p * u_prev[i] + qt * t_prev[i - t] + 1.
    print('{:.12f}'.format(t_cur[-1]))


if __name__ == '__main__':
    main()
