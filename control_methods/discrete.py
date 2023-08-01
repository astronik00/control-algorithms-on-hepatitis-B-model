import numerical_methods.euler as model


def get_psi(x1_const, x):
    return x[0][-1] - x1_const


def get_fi(a, h, l2, psi, x1_const, x1, x2, x3, x6):
    return (-a[2] * x1) ** -1 * (
                h ** -1 * (x1_const - l2 * psi - x1) - (a[0] + a[1] * x6) * x2 + a[3] * x1 + a[4] * (1 - x2 - x3) * x1)


def adar(a, h, l1, l2, xi, x1_const, x, xlag):
    psi = get_psi(x1_const, x)
    fi = get_fi(a, h, l2, psi, x1_const, x[0][-1], x[1][-1], x[2][-1], x[5][-1])
    psi1 = x[9][-1] - fi
    psi2 = 0
    fi_next = get_fi(a, h, l2, psi, x1_const, model.x1_next(a, h, x), model.x2_next(a, h, x),
                     model.x3_next(a, h, x), model.x6_next(a, xi, h, x, xlag))

    u = h * (fi_next - l1 * psi1 - x[9][-1]) - a[31] * x[8][-1] + a[32] * x[0][-1] * x[9][-1] + a[33] * x[9][-1]
    return psi, psi1, psi2, u
