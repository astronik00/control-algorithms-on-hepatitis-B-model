import numpy as np
import utils.plotter as plotter
import scheme.discrete as discrete


filepath = 'coefficients/coeffs1.txt'
a = [float(x) for x in open(filepath).read().split("\n")]
history = [1e-6, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0]

model_labels = ["V_f", "C_V", "m", "M_V", "H_E", "E", "H_B", "B", "P", "F"]
control_labels = ["t_reach", "\psi", "\psi_1", "\psi_2", "u"]

# TODO : add default values support
tstart = 0
tend = 150
h = 0.01
x1_const = 1e-8
l1 = -0.9
l2 = -0.9
c = 0.1
mean = 0.0

df_list = []
variances = [0.1, 0.3, 0.5, 0.7, 0.9, 1.2]
t_reach_time_list = []
t_reach_index_list = []
u_sum_square = []

for variance in variances:
    t, x, control = discrete.calculate([tstart, tend, h], history, a,
                                       control_params={'type': 'nas',
                                                       'x1_const': x1_const,
                                                       'l1': l1,
                                                       'l2': l2,
                                                       'c': c,
                                                       'mean': mean,
                                                       'variance': variance})
    for i in range(0, len(t)):
        if x[0][i] < x1_const:
            t_reach_time_list.append(t[i])
            t_reach_index_list.append(i)
            break

    u_sum_square.append(np.sum(np.power(control[-1][: t_reach_index_list[-1]], 2)))
    df_list.append(plotter.to_df(t, x, control, [model_labels, control_labels]))

for i in range(len(t_reach_time_list)):
    print(f't_reach: {t_reach_time_list[i]}, sigma: {variances[i]}, sum(u^2): {u_sum_square[i]}')

# plotter.plot_x(df4, 'images/nas/')
