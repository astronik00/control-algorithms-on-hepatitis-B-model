import models.hepatitis_b as model
import numerical_methods.euler as euler


def get_psi(x1_const, x1):
    return x1 - x1_const


def get_psi2(k, x1_const, x1, x11):
    return get_psi(x1_const, x1) + k * x11


def get_fi_adar(a, h, l2, x1_const, x1, x2, x3, x6):
    return (-a[2] * x1) ** -1 * (
            h ** -1 * (x1_const - l2 * get_psi(x1_const, x1) - x1) - (a[0] + a[1] * x6) * x2 + a[3] * x1 + a[4] * (
            1 - x2 - x3) * x1)


def get_fi_nad(a, k, n, h, l2, x1_const, x1, x2, x3, x6, x11, x):
    return ((-a[2] * x1) ** -1 *
            (h ** -1 * (x1_const - k * euler.x11_next(n, h, x1_const, x) - l2 * get_psi2(k, x1_const, x1, x11) - x1)
             - (a[0] + a[1] * x6) * x2 + a[3] * x1 + a[4] * (1 - x2 - x3) * x1))


def adar(a, h, l1, l2, xi, x1_const, x, xlag):
    psi_temp = get_psi(x1_const, x[0][-1])
    fi_temp = get_fi_adar(a, h, l2, x1_const, x[0][-1], x[1][-1], x[2][-1], x[5][-1])
    psi1_temp = x[9][-1] - fi_temp
    psi2_temp = 0
    fi_next = get_fi_adar(a, h, l2, x1_const,
                          euler.x1_next(a, h, x),
                          euler.x2_next(a, h, x),
                          euler.x3_next(a, h, x),
                          euler.x6_next(a, xi, h, x, xlag))

    u_temp = h * (fi_next - l1 * psi1_temp - x[9][-1]) - model.f10(a, x)

    return psi_temp, psi1_temp, psi2_temp, u_temp


def nad(a, h, k, n, l1, l2, xi, x1_const, x, xlag):
    psi_temp = get_psi(x1_const, x[0][-1])
    psi2_temp = get_psi2(k, x1_const, x[0][-1], x[10][-1])
    fi_temp = get_fi_nad(a, k, n, h, l2, x1_const, x[0][-1], x[1][-1], x[2][-1], x[5][-1], x[10][-1], x)
    psi1_temp = x[9][-1] - fi_temp

    fi_next = get_fi_nad(a, k, n, h, l2, x1_const,
                         euler.x1_next(a, h, x),
                         euler.x2_next(a, h, x),
                         euler.x3_next(a, h, x),
                         euler.x6_next(a, xi, h, x, xlag),
                         euler.x11_next(n, h, x1_const, x),
                         x)

    u_temp = h ** -1 * (-l1 * psi1_temp + fi_next - x[9][-1]) - model.f10(a, x) - x[10][-1]

    # print(u_temp)

    return psi_temp, psi1_temp, psi2_temp, u_temp


def nas(a, c, psi1_prev, h, l1, l2, xi, x1_const, x, xlag):
    psi_temp = get_psi(x1_const, x[0][-1])
    fi_temp = get_fi_adar(a, h, l2, x1_const, x[0][-1], x[1][-1], x[2][-1], x[5][-1])
    psi1_temp = x[9][-1] - fi_temp
    psi2_temp = 0
    fi_next = get_fi_adar(a, h, l2, x1_const,
                          euler.x1_next(a, h, x),
                          euler.x2_next(a, h, x),
                          euler.x3_next(a, h, x),
                          euler.x6_next(a, xi, h, x, xlag))

    u_temp = h ** -1 * (fi_next - l1 * psi1_temp - x[9][-1]) - model.f10(a, x) - h ** -1 * c * (
                psi1_temp + l1 * psi1_prev)

    # print(u_temp)

    return psi_temp, psi1_temp, psi2_temp, u_temp
