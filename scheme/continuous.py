import numpy as np
import models.hepatitis_b as model
import numerical_methods.euler as euler
import control_methods.continuous as stc


def get_delay(i: int, m: int, x: list[list], lags: list[list[list]]):
    for j in range(len(lags[0])):
        if i < m[0]:
            lags[0][j].append(x[j][0])
        else:
            lags[0][j].append(x[j][i - m[0]])

    for j in range(len(lags[1])):
        if i < m[1]:
            lags[1][j].append(x[j][0])
        else:
            lags[1][j].append(x[j][i - m[1]])

    for j in range(len(lags[2])):
        if i < m[2]:
            lags[2][j].append(x[j][0])
        else:
            lags[2][j].append(x[j][i - m[2]])

    for j in range(len(lags[3])):
        if i < m[3]:
            lags[3][j].append(x[j][0])
        else:
            lags[3][j].append(x[j][i - m[3]])

    for j in range(len(lags[4])):
        if i < m[4]:
            lags[4][j].append(x[j][0])
        else:
            lags[4][j].append(x[j][i - m[4]])

    return lags


def calculate(time, history, a, control_params=None):
    tstart = time[0]
    tend = time[1]
    h = time[2]
    t = [tstart]

    tau = [a[9], a[19], a[14], a[25], a[29]]
    m = np.int32(np.divide(tau, h))
    points = int((tend - tstart) / h)

    control = [[0], [0], [0], [0]]

    if control_params is not None:
        if control_params['type'] == 'nad':
            x = ([history[0]], [history[1]], [history[2]], [history[3]], [history[4]],
                 [history[5]], [history[6]], [history[7]], [history[8]], [history[9]],
                 [history[10]])

            xlag = [[[], [], [], [], [], [], [], [], [], [], []],
                    [[], [], [], [], [], [], [], [], [], [], []],
                    [[], [], [], [], [], [], [], [], [], [], []],
                    [[], [], [], [], [], [], [], [], [], [], []],
                    [[], [], [], [], [], [], [], [], [], []], []]
        else:
            x = ([history[0]], [history[1]], [history[2]], [history[3]], [history[4]],
                 [history[5]], [history[6]], [history[7]], [history[8]], [history[9]])

            xlag = [[[], [], [], [], [], [], [], [], [], []],
                    [[], [], [], [], [], [], [], [], [], []],
                    [[], [], [], [], [], [], [], [], [], []],
                    [[], [], [], [], [], [], [], [], [], []],
                    [[], [], [], [], [], [], [], [], [], []]]

    else:
        x = ([history[0]], [history[1]], [history[2]], [history[3]], [history[4]],
             [history[5]], [history[6]], [history[7]], [history[8]], [history[9]])

        xlag = [[[], [], [], [], [], [], [], [], [], []],
                [[], [], [], [], [], [], [], [], [], []],
                [[], [], [], [], [], [], [], [], [], []],
                [[], [], [], [], [], [], [], [], [], []],
                [[], [], [], [], [], [], [], [], [], []]]

    for i in range(points):
        try:
            xlag = get_delay(i, m, x, xlag)

            xi = model.get_xi(x, 0.5)

            x1_const, psi, psi1, psi2, u, disturbance = 0, 0, 0, 0, 0, 0

            if control_params is not None:
                x1_const = control_params['x1_const']
                T1 = control_params['T1']
                T2 = control_params['T2']

                if control_params['type'] == 'adar':
                    psi, psi1, psi2, u = stc.adar(a, T1, T2, xi, x1_const, x, xlag)
                    disturbance = 0

                # TODO : doesn't work properly
                elif control_params['type'] == 'nad':
                    k = control_params['k']
                    n = control_params['n']
                    psi, psi1, psi2, u = stc.nad(a, k, n, T1, T2, xi, x1_const, x, xlag)
                    disturbance = 0.1

                if u < 0:
                    u = 0
                elif u > 20:
                    u = 20

            control[0].append(psi)
            control[1].append(psi1)
            control[2].append(psi2)
            control[3].append(u)

            x[0].append(euler.x1_next(a, h, x))
            x[1].append(euler.x2_next(a, h, x))
            x[2].append(euler.x3_next(a, h, x))
            x[3].append(euler.x4_next(a, h, x))
            x[4].append(euler.x5_next(a, xi, h, x, xlag))
            x[5].append(euler.x6_next(a, xi, h, x, xlag))
            x[6].append(euler.x7_next(a, xi, h, x, xlag))
            x[7].append(euler.x8_next(a, xi, h, x, xlag))
            x[8].append(euler.x9_next(a, xi, h, x, xlag))
            x[9].append(euler.x10_next(a, h, x, u, disturbance))

            if control_params is not None:
                if control_params['type'] == 'nad':
                    x[10].append(euler.x11_next(a, h, x1_const, x))

            t.append(tstart + (i + 1) * h)

        except Exception as e:
            print(f"CalculationError: {e.args[0]}")
            break

    return t, x, control
