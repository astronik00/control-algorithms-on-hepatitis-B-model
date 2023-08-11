import numpy as np
import utils.plotter as plotter
import matplotlib.pyplot as plt
import scheme.discrete as discrete

filepath = '../../coefficients/coeffs2.txt'
a = [float(x) for x in open(filepath).read().split("\n")]
history = [1e-6, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0]

model_labels = ["V_f", "C_V", "m", "M_V", "H_E", "E", "H_B", "B", "P", "F", "Z"]
control_labels = ["\psi", "\psi_1", "\psi_2", "u"]
measure_labels = ['days', 'particle/ml', 'cell/ml', 'cell/ml', 'cell/ml', 'cell/ml', 'cell/ml', 'cell/ml', 'cell/ml',
                  'cell/ml', 'molecule/ml', '', '', '', '', 'molecule/ml']

# l1 = 0.001, l2 = -0.997
t, t_reach, x, control, disturbances_list = discrete.calculate([0, 200, 0.01],
                                                               history,
                                                               a,
                                                               control_params={
                                                                   'type': 'nas',
                                                                   'x1_const': 1e-8,
                                                                   'b': 25,
                                                                   'l1': -0.9,
                                                                   'l2': -0.995,
                                                                   'mean': 0.0,
                                                                   'variance': 0.05,
                                                                   'c': 0.1
                                                               })


df = plotter.to_df(t, x, control, [model_labels, control_labels])
plotter.plot_x(df, '../../images/nas/', measure_labels)
