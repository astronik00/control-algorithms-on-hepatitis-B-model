import models.hepatitis_b as model


def x1_next(a, h, x):
    return x[0][-1] + h * model.f1(a, x)


def x2_next(a, h, x):
    return x[1][-1] + h * model.f2(a, x)


def x3_next(a, h, x):
    return x[2][-1] + h * model.f3(a, x)


def x4_next(a, h, x):
    return x[3][-1] + h * model.f4(a, x)


def x5_next(a, xi, h, x, xlag):
    return x[4][-1] + h * model.f5(a, xi, x, xlag)


def x6_next(a, xi, h, x, xlag):
    return x[5][-1] + h * model.f6(a, xi, x, xlag)


def x7_next(a, xi, h, x, xlag):
    return x[6][-1] + h * model.f7(a, xi, x, xlag)


def x8_next(a, xi, h, x, xlag):
    return x[7][-1] + h * model.f8(a, xi, x, xlag)


def x9_next(a, xi, h, x, xlag):
    return x[8][-1] + h * model.f9(a, xi, x, xlag)


def x10_next(a, h, x, u, disturbance1=None, disturbance2=None):
    return x[9][-1] + h * (model.f10(a, x) + u + disturbance1 + disturbance2)


def x11_next(n, h, x1_const, x):
    return x[10][-1] + h * model.f11(n, x1_const, x[0][-1])
