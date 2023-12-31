import os
import utils.plotter as plotter
import scheme.continuous as continuous


def run(images_filepath, coefficients_filepath):
    model_labels = ["V_f", "C_V", "m", "M_V", "H_E", "E", "H_B", "B", "P", "F"]
    control_labels = ["\psi", "\psi_1", "\psi_2", "u"]

    # default initial values of hepatitis B model variables
    history = [1e-6, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    flag = True

    # TODO : add default values support
    # tstart = 0
    # tend = 150
    # h = 0.01
    # x1_const = 1e-8
    # T1 = 0.7
    # T2 = 1.0

    a = [float(x) for x in open(coefficients_filepath).read().split("\n")]

    while flag:
        user_number = int(input('1 - no control\n2 - ADAR control\n0 - exit\n>>> '))

        if user_number == 1:
            tstart = int(input('Time start:\n>>> '))
            tend = int(input('Time end:\n>>> '))
            h = float(input('Time step:\n>>> '))

            input_history = [float(item) for item in input(
                'History values: (press \'enter\' to use default history [1e-6, 0, 0, 1, 1, 1, 1, 1, 1, 1])\n>>> ').split()]

            if len(input_history) == 10:
                history = input_history
            elif input_history:
                print("IncorrectFormat: used default history vector: [1e-6, 0, 0, 1, 1, 1, 1, 1, 1, 1]")

            t, x, control = continuous.calculate([tstart, tend, h], history, a)
            df = plotter.to_df(t, x, control, [model_labels, control_labels])
            plotter.plot_x(df, images_filepath + 'no_control/')
            print('Successfully calculated hepatitis B acute stage without control\n')

        elif user_number == 2:
            tstart = int(input('Time start:\n>>> '))
            tend = int(input('Time end:\n>>> '))
            h = float(input('Time step:\n>>> '))
            x1_const = float(input('Target value:\n>>> '))
            T1 = float(input('Parameter T1:\n>>> '))
            T2 = float(input('Parameter T2:\n>>> '))

            input_history = [float(item) for item in input(
                'History values: (press \'enter\' to use default history [1e-6, 0, 0, 0, 1, 1, 1, 1, 1, 1])\n>>> ')
            .split()]

            if len(input_history) == 10:
                history = input_history
            elif input_history:
                print("IncorrectFormat: used default history vector: [1e-6, 0, 0, 0, 1, 1, 1, 1, 1, 1]")

            t, x, control = continuous.calculate([tstart, tend, h], history, a,
                                                 control_params={'type': 'adar', 'x1_const': x1_const, 'T1': T1,
                                                                 'T2': T2})

            df = plotter.to_df(t, x, control, [model_labels, control_labels])
            plotter.plot_x(df, images_filepath + 'adar/')
            print('Successfully calculated hepatitis B acute stage with ADAR control\n')

        else:
            flag = False
