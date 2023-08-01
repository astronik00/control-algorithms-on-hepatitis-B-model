import numpy as np
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


def plot_two(df1, df2, workdir):
    if df1.shape[1] != df2.shape[1]:
        raise Exception("Can't ffs")

    for i in range(1, df1.shape[1]):
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()

        ax1.plot(df1.iloc[1::, 0], df1.iloc[1::, i], linestyle="-", linewidth=1.9, color="red", alpha=0.85)
        ax2.plot(df2.iloc[1::, 0], df2.iloc[1::, i], linestyle="-", linewidth=1.9, color="darkturquoise", alpha=0.85)

        if i == 1:
            ax2.plot(df1.iloc[1::, 0], np.zeros(df1.shape[0] - 1), linewidth=5.0, color="red", alpha=0.8)

        ylimit1 = max(df1.iloc[0::, i]) * 1.2
        ylimit2 = max(df2.iloc[0::, i]) * 1.2

        ax1.set_ylim(min(df1.iloc[1::, i]), ylimit1)
        ax2.set_ylim(min(df2.iloc[1::, i]), ylimit2)

        ax1.set_xlabel("$t$, days", loc="right")
        ax1.text(.01, .97, "$" + str(df1.columns[i]) + "(t)$", ha='left', va='top', transform=ax1.transAxes)

        fig.tight_layout()
        fig.savefig(workdir + "png/" + str(df1.columns[i]) + ".png")
        fig.savefig(workdir + "svg/" + str(df1.columns[i]) + ".svg")
        # plt.show()
        plt.close()
