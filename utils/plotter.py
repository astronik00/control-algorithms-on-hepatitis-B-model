import pandas as pd
import matplotlib.pyplot as plt


def to_df(t, x, control, labels):
    model_labels = labels[0]
    control_labels = labels[1]

    x_dict = {"t": t}
    control_dict = {}

    for i in range(len(x)):
        x_dict[model_labels[i]] = x[i]

    for i in range(len(control)):
        control_dict[control_labels[i]] = control[i]

    return pd.concat([pd.DataFrame(x_dict), pd.DataFrame(control_dict)], axis=1)


def plot_x(df, workdir):
    for i in range(1, df.shape[1]):
        fig, ax = plt.subplots()

        ax.plot(df.iloc[1::, 0], df.iloc[1::, i], linewidth=2.0, color="black")

        ylimit = max(df.iloc[0::, i]) * 1.2
        ax.set_ylim(min(df.iloc[1::, i]), ylimit)

        ax.set_xlabel("$t$, days", loc="right")
        ax.text(.01, .97, "$" + str(df.columns[i]) + "(t)$", ha='left', va='top', transform=ax.transAxes)

        fig.tight_layout()
        fig.savefig(workdir + "png/" + str(df.columns[i]) + ".png")
        fig.savefig(workdir + "svg/" + str(df.columns[i]) + ".svg")
        # plt.show()
        plt.close()
