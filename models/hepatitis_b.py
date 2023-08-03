def get_xi(x, threshold):
    if x[2][-1] < 0:
        raise Exception(f"m is out of range. Expected: [0; 1], actual: {x[2][-1]}")
    if x[2][-1] >= 1:
        raise Exception(f"patient has died")
    return 1 if 0 <= x[2][-1] < threshold else (x[2][-1] - 1) / (threshold - 1)


def f1(a, x):
    return ((a[0] + a[1] * x[5][-1]) * x[1][-1] - a[2] * x[0][-1] * x[9][-1]
            - a[3] * x[0][-1] - a[4] * (1 - x[1][-1] - x[2][-1]) * x[0][-1])


def f2(a, x):
    return a[34] * (1 - x[1][-1] - x[2][-1]) * x[0][-1] - a[35] * x[1][-1] * x[5][-1] - a[36] * x[1][-1]


def f3(a, x):
    return a[35] * x[1][-1] * x[5][-1] + a[36] * x[1][-1] - a[37] * x[2][-1]


def f4(a, x):
    return a[5] * x[0][-1] - a[6] * x[3][-1] - a[7] * x[3][-1] * x[5][-1]


def f5(a, xi, x, xlag):
    return (a[8] * xi * xlag[0][3][-1] * xlag[0][4][-1] - a[10] * x[3][-1] * x[4][-1]
            - a[11] * x[3][-1] * x[4][-1] * x[5][-1] + a[12] * (1 - x[4][-1]))


def f6(a, xi, x, xlag):
    return (a[18] * xi * xlag[1][3][-1] * xlag[1][4][-1] * xlag[1][5][-1] -
            a[20] * x[3][-1] * x[4][-1] * x[5][-1] - a[21] * x[1][-1] * x[5][-1]
            - a[22] * x[3][-1] * x[5][-1] + a[23] * (1 - x[5][-1]))


def f7(a, xi, x, xlag):
    return (a[13] * xi * xlag[2][3][-1] * xlag[2][6][-1] - a[15] * x[3][-1] * x[6][-1]
            - a[16] * x[3][-1] * x[6][-1] * x[7][-1] + a[17] * (1 - x[6][-1]))


def f8(a, xi, x, xlag):
    return (a[24] * xi * xlag[3][3][-1] * xlag[3][6][-1] * xlag[3][7][-1]
            - a[26] * x[3][-1] * x[6][-1] * x[7][-1] + a[27] * (1 - x[7][-1]))


def f9(a, xi, x, xlag):
    return a[28] * xi * xlag[4][3][-1] * xlag[4][6][-1] * xlag[4][7][-1] + a[30] * (1 - x[8][-1])


def f10(a, x):
    return a[31] * x[8][-1] - a[32] * x[0][-1] * x[9][-1] - a[33] * x[9][-1]


def f11(n, x1_const, x1):
    return n * (x1 - x1_const)
