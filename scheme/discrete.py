import random
import numpy as np
import models.hepatitis_b as model
import numerical_methods.euler as euler
import synergetic_control.discrete.control as stc


def get_delay(i, m, x, lags):
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


def calculate(time, history, a, control_params=None, disturbances=None):
    tstart = time[0]
    tend = time[1]
    h = time[2]
    t = [tstart]
    t_reach = -1

    tau = [a[9], a[19], a[14], a[25], a[29]]
    m = np.int32(np.divide(tau, h))
    points = int((tend - tstart) / h)

    disturbances_list = [[0], [0]]
    control = [[0], [0], [0], [0]]
    psi1_prev = [0]

    x = ([history[0]], [history[1]], [history[2]], [history[3]], [history[4]],
         [history[5]], [history[6]], [history[7]], [history[8]], [history[9]],
         [history[10]])

    xlag = [[[], [], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], [], []],
            [[], [], [], [], [], [], [], [], [], []], []]

    for i in range(points):
        try:
            # print(i)
            xlag = get_delay(i, m, x, xlag)

            xi = model.get_xi(0.5, x)

            n, k, psi, psi1, psi2, u, disturbance1, disturbance2 = 0, 0, 0, 0, 0, 0, 0, 0

            #if t[-1] >= 65 and t[i] <= 120:
            if control_params is not None:
                x1_const = control_params['x1_const']
                l1 = control_params['l1']
                l2 = control_params['l2']
                b = control_params['b']

                if x[0][-1] - x1_const < 1e-11 or x[0][-1] < x1_const:
                    t_reach = t[-1]


                if control_params['type'] == 'adar':
                    psi, psi1, psi2, u = stc.adar(a, h, l1, l2, xi, x1_const, x, xlag)

                    if disturbances is not None:
                        disturbance1 = disturbances[0][i]
                        disturbance2 = disturbances[1][i]

                elif control_params['type'] == 'nad':
                    k = control_params['k']
                    n = control_params['n']
                    disturbance1 = control_params['disturbance']
                    # disturbance1 = math.sin(math.pi * t[-1] / 2)
                    psi, psi1, psi2, u = stc.nad(a, h, k, n, l1, l2, xi, x1_const, x, xlag)

                elif control_params['type'] == 'nas':
                    c = control_params['c']
                    mean = control_params['mean']
                    variance = control_params['variance']
                    disturbance1 = random.normalvariate(mean, variance)
                    disturbance2 = random.normalvariate(mean, variance)

                    disturbances_list[0].append(disturbance1)
                    disturbances_list[1].append(disturbance2)
                    psi, psi1, psi2, u = stc.nas(a, c, psi1_prev[-1], h, l1, l2, xi, x1_const, x, xlag)


                if b != -1:
                    if u < 0:
                        u = 0
                    elif u > b:
                        u = b
                #
                # if u < 0:
                #     u = 0

            if t_reach != -1:
                break

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
            psi1_prev.append(control[1][i])

            if control_params is not None:
                if control_params['type'] == 'nas':
                    x[9].append(euler.x10_next(a, h, x, u, disturbance1, disturbance2))
                    x[10].append(0)
                elif control_params['type'] == 'nad':
                    x1_const = control_params['x1_const']
                    x[9].append(euler.x10_next(a, h, x, u, disturbance1))
                    x[10].append(euler.x11_next(n, h, x1_const, x))
                elif control_params['type'] == 'adar':
                    x[9].append(euler.x10_next(a, h, x, u))
                    x[10].append(0)
            else:
                x[9].append(euler.x10_next(a, h, x, 0))
                x[10].append(0)

            t.append(tstart + (i + 1) * h)

            # if x[0][-1] < x1_const:
            #     t_reach = [i, t[-1]]

        except Exception as e:
            print(f"CalculationError: {e.args[0]}")
            break

    return t, t_reach, x, control, disturbances_list
