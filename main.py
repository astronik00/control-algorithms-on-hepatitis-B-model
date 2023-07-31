import utils.plotter as plotter
from scheme.different_delays import calculate

filepath = 'coefficients/coeffs1.txt'
a = [float(x) for x in open(filepath).read().split("\n")]
history = [1e-6, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]

model_labels = ["V_f", "C_V", "m", "M_V", "H_E", "E", "H_B", "B", "P", "F"]
control_labels = ["\psi", "\psi_1", "\psi_2", "u"]

# t, x, control = calculate([0, 150, 0.01], history, a)
# df = plotter.to_df(t, x, control, [model_labels, control_labels])
# plotter.plot_x(df, 'images/no_control/')

t, x, control = calculate([0, 150, 0.01], history, a,
                          control_params={'type': 'adar', 'x1_const': 1e-8, 'T1': 0.7, 'T2': 1.0})
df1 = plotter.to_df(t, x, control, [model_labels, control_labels])
plotter.plot_x(df1, 'images/adar/')