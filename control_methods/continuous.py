import models.hepatitis_b as model


def psi(x1_const, x):
    return x[0][-1] - x1_const


def adar(a, T1, T2, xi, x1_const, x, xlag):
    _psi = psi(x1_const, x)
    fi = (-a[2] * x[0][-1]) ** -1 * \
         (-_psi * T2 ** -1 - (a[0] + a[1] * x[5][-1]) * x[1][-1]
          + a[3] * x[0][-1] + a[4] * (1 - x[1][-1] - x[2][-1]) * x[0][-1])

    _psi1 = x[9][-1] - fi
    _psi2 = 0  # not used

    # exact differential
    x1_d = (a[2] * T2 * x[0][-1] ** 2) ** -1 * (x1_const - T2 * x[1][-1] * (a[0] + a[1] * x[5][-1])) * model.f1(a, x)
    x2_d = ((a[2] * x[0][-1]) ** -1 * (a[0] + a[1] * x[5][-1]) + a[4] / a[2]) * model.f2(a, x)
    x3_d = (a[4] / a[2]) * model.f3(a, x)
    x6_d = ((a[2] * x[0][-1]) ** -1 * (a[1] * x[1][-1])) * model.f6(a, xi, x, xlag)
    fi_d = x1_d + x2_d + x3_d + x6_d

    u = fi_d - _psi1*T1**-1 - a[31]*x[8][-1] + a[32]*x[0][-1]*x[9][-1] + a[33]*x[9][-1]
    return _psi, _psi1, _psi2, u


def nad(a, k, n, T1, T2, ksi, x1_const, x, xlag):
    _psi = psi(x1_const, x)
    _psi2 = _psi + k*x[10][-1]

    # print(f"psi2 = {_psi2}")

    fi = (-a[2]*x[0][-1])**-1 * (-_psi2*T2**-1 - (a[0] + a[1]*x[5][-1])*x[1][-1] + a[3]*x[0][-1] + a[4]*(1 - x[1][-1] - x[2][-1])*x[0][-1] - k*n*_psi)
    _psi1 = x[9][-1] - fi

    # exact differential
    x1_d =  ((-a[2]*T2*x[0][-1]**2)**-1 * (x1_const*(1 + k*n*T2) - k*x[10][-1] - x[1][-1]*T2*(a[0] + a[1]*x[5][-1]))) * model.f1(a, x)
    x2_d = ((a[2]*x[0][-1])**-1 * (a[0] + a[1]*x[5][-1]) + a[4] / a[2]) * model.f2(a, x)
    x3_d = (a[4] / a[2]) * model.f3(a, x)
    x6_d = ((a[2]*x[0][-1])**-1 * (a[1]*x[1][-1])) * model.f6(a, ksi, x, xlag)
    x11_d = (a[2]*x[0][-1]*T2)**-1 * k * model.f11(a, x1_const, x)
    fi_d = x1_d + x2_d + x3_d + x6_d + x11_d

    u = fi_d - _psi1*T1**-1 - a[31]*x[8][-1] + a[32]*x[0][-1]*x[9][-1] + a[33]*x[9][-1] - x[10][-1]
    return _psi, _psi1, _psi2, u