import utils.plotter as plotter
import scheme.discrete as discrete
import scheme.continuous as continuous

filepath = '../../coefficients/coeffs2.txt'
a = [float(x) for x in open(filepath).read().split("\n")]
history = [1e-6, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0]

model_labels= ["V_f", "C_V", "m", "M_V", "H_E", "E", "H_B", "B", "P", "F", "Z"]
control_labels = ["\psi", "\psi_1", "\psi_2", "u"]

# l1 = -0.1, l2 = -0.2
t, t_reach, x, control, disturbances_list = discrete.calculate([0, 150, 0.01],
                                                               history,
                                                               a,
                                                               control_params={'b': 25,
                                                                               'type': 'adar',
                                                                               'x1_const': 1e-8,
                                                                               'l1': -0.8,
                                                                               'l2': -0.2})

df = plotter.to_df(t, x, control, [model_labels, control_labels])
plotter.plot_x(df, '../../images/adar/')

# t, x, control = continuous.calculate([0, 150, 0.01],
#                                      history,
#                                      a,
#                                      control_params={'type': 'adar',
#                                                      'restricted': True,
#                                                      'b': 25,
#                                                      'x1_const': 1e-8,
#                                                      'T1': 1.1,
#                                                      'T2': 0.4})
# df1 = plotter.to_df(t, x, control, [model_labels, control_labels])
# plotter.plot_x(df1, '../../images/adar/')
#
# print(min(x[0]))
