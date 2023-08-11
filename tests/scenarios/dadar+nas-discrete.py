import os
import numpy as np
import matplotlib.pyplot as plt
import utils.plotter as plotter
import scheme.discrete as discrete

filepath = '../../coefficients/coeffs2.txt'
a = [float(x) for x in open(filepath).read().split("\n")]
history = [1e-6, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0]

model_labels = ["V_f", "C_V", "m", "M_V", "H_E", "E", "H_B", "B", "P", "F", "Z"]
control_labels = ["\psi", "\psi_1", "\psi_2", "u"]
measure_labels = ['days', 'particle/ml', 'cell/ml', 'cell/ml',
                  'cell/ml', 'cell/ml', 'cell/ml', 'cell/ml',
                  'cell/ml', 'cell/ml', 'molecule/ml', '',
                  '', '', '', 'molecule/ml']
images_paths = ['../images/nas+dadar/png', '../images/nas+dadar/svg']

# create required paths if not exist
for path in images_paths:
    if not os.path.exists(path):
        os.makedirs(path)

t, t_reach, x, control, disturbances = discrete.calculate(time=[0, 600, 0.01],
                                                          history=history,
                                                          a=a,
                                                          control_params={
                                                              'type': 'nas',
                                                              'x1_const': 1e-8,
                                                              'b': 25,
                                                              'l1': -0.9,
                                                              'l2': -0.9,
                                                              'mean': 0.0,
                                                              'variance': 0.05,
                                                              'c': 0.1
                                                          })

df_nas = plotter.to_df(t, x, control, [model_labels, control_labels])


t, t_reach, x, control, disturbances = discrete.calculate(time=[0, 600, 0.01],
                                                          history=history,
                                                          disturbances=disturbances,
                                                          a=a,
                                                          control_params=
                                                          {
                                                              'type': 'adar',
                                                              'b': 25,
                                                              'x1_const': 1e-8,
                                                              'l1': -0.1,
                                                              'l2': -0.2
                                                          })

df_dadar = plotter.to_df(t, x, control, [model_labels, control_labels])

plotter.plot_two_one_axes(df_dadar, df_nas, '../images/nas+dadar/', measure_labels)
