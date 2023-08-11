import numpy as np
import utils.plotter as plotter
import matplotlib.pyplot as plt
import scheme.discrete as discrete
import scheme.continuous as continuous

filepath = '../../coefficients/coeffs2.txt'
a = [float(x) for x in open(filepath).read().split("\n")]
history = [1e-6, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0]

model_labels = ["V_f", "C_V", "m", "M_V", "H_E", "E", "H_B", "B", "P", "F", "Z"]
control_labels = ["\psi", "\psi_1", "\psi_2", "u"]
measure_labels = ['days', 'particle/ml', 'cell/ml', 'cell/ml', 'cell/ml', 'cell/ml', 'cell/ml', 'cell/ml', 'cell/ml',
                  'cell/ml', 'molecule/ml', '', '', '', '', 'molecule/ml']

# t, t_reach, x, control, disturbances_list = discrete.calculate([0, 12, 0.01],
#                                                                history,
#                                                                a,
#                                                                control_params={'type': 'nad',
#                                                                                'b': 25,
#                                                                                'x1_const': 1e-8,
#                                                                                'k': 0.001,
#                                                                                'n': 0.01,
#                                                                                'l1': -0.996,
#                                                                                'l2': -0.99,
#                                                                                'disturbance': 0.1})
#
# df = plotter.to_df(t, x, control, [model_labels, control_labels])
# plotter.plot_x(df, '../images/nad/', measure_labels)


# t, x, control = continuous.calculate(time=[0, 20, 0.01],
#                                      history=[1e-6, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
#                                      a=a,
#                                      control_params={'type': 'nad',
#                                                      'restricted': True,
#                                                      'b': 25,
#                                                      'x1_const': 1e-8,
#                                                      'k': 0.1,
#                                                      'n': 0.1,
#                                                      'T1': 0.5,
#                                                      'T2': 0.2,
#                                                      'disturbance_type': 'harmonic',
#                                                      })
#
# df_nad_harmonic = plotter.to_df(t, x, control, [model_labels, control_labels])
# plotter.plot_x(df_nad_harmonic, '../../images/nad/', measure_labels)
