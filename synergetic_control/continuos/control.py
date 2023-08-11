from models.hepatitis_b import f1
import models.hepatitis_b as model
from synergetic_control.utils import get_psi, get_psi1, get_psi2


def get_fi_nad(a: list[float], T2: float, psi: float, psi2: float, k: float, n: float, x: list[list]):
    return (-a[2] * x[0][-1]) ** -1 * (-psi2 * T2 ** -1 - f1(a, x) - k * n * psi)


def adar(a, T1, T2, xi, x1_const, x, xlag):
    psi = get_psi(x1_const, x[0][-1])

    fi = (-a[2] * x[0][-1]) ** -1 * \
         (-psi * T2 ** -1 - (a[0] + a[1] * x[5][-1]) * x[1][-1]
          + a[3] * x[0][-1] + a[4] * (1 - x[1][-1] - x[2][-1]) * x[0][-1])

    psi1 = get_psi1(fi, x[9][-1])
    psi2 = 0  # not used

    # exact differential
    x1_d = (a[2] * T2 * x[0][-1] ** 2) ** -1 * (x1_const - T2 * x[1][-1] * (a[0] + a[1] * x[5][-1])) * model.f1(a, x)
    x2_d = ((a[2] * x[0][-1]) ** -1 * (a[0] + a[1] * x[5][-1]) + a[4] / a[2]) * model.f2(a, x)
    x3_d = (a[4] / a[2]) * model.f3(a, x)
    x6_d = ((a[2] * x[0][-1]) ** -1 * (a[1] * x[1][-1])) * model.f6(a, xi, x, xlag)
    fi_d = x1_d + x2_d + x3_d + x6_d

    u = fi_d - psi1*T1**-1 - a[31]*x[8][-1] + a[32]*x[0][-1]*x[9][-1] + a[33]*x[9][-1]
    return psi, psi1, psi2, u


def nad(a, k, n, T1, T2, xi, x1_const, x, xlag, d_lst=None):
    x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11 = (x[0][-1], x[1][-1], x[2][-1],
                                                    x[3][-1], x[4][-1], x[5][-1],
                                                    x[6][-1], x[7][-1], x[8][-1],
                                                    x[9][-1], x[10][-1])

    psi = get_psi(x1_const, x1)
    psi2 = get_psi2(psi, k, x11)
    fi = get_fi_nad(a, T2, psi, psi2, k, n, x)
    psi1 = get_psi1(fi, x10)

    # exact differential
    x1_d = (a[2] * T2 * x1 ** 2) ** -1 * (x1_const * (1 + T2 * k * n) - k * x11 - x2 * T2 * (a[0] + a[1]*x6)) * model.f1(a, x)
    x2_d = ((a[2] * x1) ** -1 * (a[0] + a[1] * x6) + a[4] / a[2]) * model.f2(a, x)
    x3_d = a[4] / a[2] * model.f3(a, x)
    x6_d = (a[2] * x1) ** -1 * (a[1] * x2) * model.f6(a, xi, x, xlag)
    x11_d = (a[2] * x1 * T2) ** -1 * k * model.f11(n, x1_const, x1)

    if d_lst is not None:
        fi_d = x1_d * d_lst[0] + x2_d * d_lst[1] + x3_d * d_lst[2] + x6_d * d_lst[3] + x11_d * d_lst[4]
    else:
        fi_d = x1_d + x2_d + x3_d + x6_d + x11_d

    u = fi_d - psi1 * T1 ** -1 - model.f10(a, x) - x11

    # print(f"psi = {psi}, psi1 = {psi1}, psi2 = {psi2}, u = {u}")

    return psi, psi1, psi2, u