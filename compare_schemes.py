import utils.plotter as plotter
import scheme.discrete as discrete
import scheme.continuous as continious

filepath = 'coefficients/coeffs1.txt'
a = [float(x) for x in open(filepath).read().split("\n")]
history = [1e-6, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0]

model_labels = ["V_f", "C_V", "m", "M_V", "H_E", "E", "H_B", "B", "P", "F"]
model_labels_nad = ["V_f", "C_V", "m", "M_V", "H_E", "E", "H_B", "B", "P", "F", "Z"]
control_labels = ["\psi", "\psi_1", "\psi_2", "u"]

# t, x, control = continious.calculate([0, 150, 0.01], history, a,
#                                      control_params={'type': 'adar', 'x1_const': 1e-8, 'T1': 0.7, 'T2': 1.0})
# df1 = plotter.to_df(t, x, control, [model_labels, control_labels])
#
# t, x, control = discrete.calculate([0, 150, 0.01], history, a,
#                                    control_params={'type': 'adar', 'x1_const': 1e-8, 'l1': -0.1, 'l2': -0.2})
# df2 = plotter.to_df(t, x, control, [model_labels, control_labels])
#
# plotter.plot_two(df1, df2, 'images/adar+dadar/')

# t, x, control = discrete.calculate([0, 350, 0.01], history, a,
#                                      control_params={'type': 'nad',
#                                                      'x1_const': 1e-8,
#                                                      'l1': -0.9,
#                                                      'l2': -0.9,
#                                                      'k': 0.1,
#                                                      'n': 0.1,
#                                                      'disturbance': 0.1})

t, x, control = discrete.calculate([0, 120, 0.01], history, a,
                                   control_params={'type': 'nas',
                                                   'x1_const': 1e-8,
                                                   'l1': -0.9,
                                                   'l2': -0.9,
                                                   'c': 0.1,
                                                   'mean': 0,
                                                   'variance': 1.0})

df4 = plotter.to_df(t, x, control, [model_labels, control_labels])
plotter.plot_x(df4, 'images/nas/')
