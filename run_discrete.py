import os
import utils.plotter as plotter
import scheme.discrete as discrete


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
        user_number = int(input('1 - no control\n2 - ADAR control\n3 - NAD control\n4 - NAS control\n0 - exit\n>>> '))

        if user_number == 1:
            tstart = int(input('Time start:\n>>> '))
            tend = int(input('Time end:\n>>> '))
            h = float(input('Time step:\n>>> '))

            input_history = [float(item) for item in input(
                'History values: (hit \'enter\' to use default history [1e-6, 0, 0, 1, 1, 1, 1, 1, 1, 1])\n>>> ').split()]

            if len(input_history) == 10:
                history = input_history
            elif input_history:
                print("IncorrectFormat: used default history vector: [1e-6, 0, 0, 1, 1, 1, 1, 1, 1, 1]")

            t, x, control = discrete.calculate([tstart, tend, h], history, a)
            df = plotter.to_df(t, x, control, [model_labels, control_labels])
            plotter.plot_x(df, images_filepath + 'no_control/')
            print('Successfully calculated hepatitis B acute stage without control\n')

        elif user_number == 2:
            tstart = int(input('Time start:\n>>> '))
            tend = int(input('Time end:\n>>> '))
            h = float(input('Time step:\n>>> '))
            x1_const = float(input('Target value:\n>>> '))
            l1 = float(input('Parameter l1 (-1 < l1 < 1):\n>>> '))
            l2 = float(input('Parameter l2 (-1 < l2 < 1):\n>>> '))

            input_history = [float(item) for item in input(
                'History values: (hit \'enter\' to use default history [1e-6, 0, 0, 0, 1, 1, 1, 1, 1, 1])\n>>> ')
            .split()]

            if len(input_history) == 10:
                history = input_history
            elif input_history:
                print("IncorrectFormat: used default history vector: [1e-6, 0, 0, 0, 1, 1, 1, 1, 1, 1]")

            t, x, control = discrete.calculate([tstart, tend, h], history, a,
                                               control_params={'type': 'adar', 'x1_const': x1_const, 'l1': l1, 'l2': l2})

            df = plotter.to_df(t, x, control, [model_labels, control_labels])
            plotter.plot_x(df, images_filepath + 'adar/')
            print('Successfully calculated hepatitis B acute stage with ADAR control\n')

        elif user_number == 3:
            tstart = int(input('Time start:\n>>> '))
            tend = int(input('Time end:\n>>> '))
            h = float(input('Time step:\n>>> '))
            x1_const = float(input('Target value:\n>>> '))
            l1 = float(input('Parameter l1 (-1 < l1 < 1):\n>>> '))
            l2 = float(input('Parameter l2 (-1 < l2 < 1):\n>>> '))

            input_history = [float(item) for item in input(
                'History values: (hit \'enter\' to use default history [1e-6, 0, 0, 0, 1, 1, 1, 1, 1, 1])\n>>> ')
            .split()]

            k = float(input('Parameter k (k > 0):\n>>> '))
            n = float(input('Parameter n (n > 0):\n>>> '))
            disturbance = float(input('Disturbance eta :\n>>> '))

            t, x, control = discrete.calculate([tstart, tend, h], history, a,
                                               control_params={'type': 'adar',
                                                               'x1_const': x1_const,
                                                               'l1': l1,
                                                               'l2': l2,
                                                               'k' : k,
                                                               'n': n,
                                                               'disturbance': disturbance})

        elif user_number == 4:
            tstart = int(input('Time start:\n>>> '))
            tend = int(input('Time end:\n>>> '))
            h = float(input('Time step:\n>>> '))
            x1_const = float(input('Target value:\n>>> '))
            l1 = float(input('Parameter l1 (-1 < l1 < 1):\n>>> '))
            l2 = float(input('Parameter l2 (-1 < l2 < 1):\n>>> '))

            input_history = [float(item) for item in input(
                'History values: (hit \'enter\' to use default history [1e-6, 0, 0, 0, 1, 1, 1, 1, 1, 1])\n>>> ')
            .split()]

            c = float(input('Parameter k (k > 0):\n>>> '))
            mean = float(input('Mathematical expectation:\n>>> '))
            variance = float(input('Statistical dispersion:\n>>> '))

            t, x, control = discrete.calculate([tstart, tend, h], history, a,
                                               control_params={'type': 'adar',
                                                               'x1_const': x1_const,
                                                               'l1': l1,
                                                               'l2': l2,
                                                               'c': c,
                                                               'mean': mean,
                                                               'variance': variance})
        else:
            flag = False
