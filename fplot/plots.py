import argparse
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import gridspec
from collections import namedtuple

sns.set_style("white")
sns.set_context("talk")
sns.set_style("ticks")

class PlotInfo(object):
    def __init__(self):
        self.x_labels = None
        self.x_label = None
        self.x_ticks = None
        self.rotate_x_labels = None

        self.y_label = None
        self.y_labels = None
        self.y_ticks = None
        self.rotate_y_labels = None


def __get_plot_info(plot_info):
    pi = PlotInfo()

    names = [a for a in dir(pi) if not a.startswith('__')]

    for n in names:
        if n in plot_info:
            pi.__setattr__(n, plot_info[n])

    return pi


def __render_x_labels(pi, ax):
    if pi.x_labels:
        ax.set_xticks(np.arange(len(pi.x_labels)))
        ax.set_xticklabels(list(pi.x_labels))
    else:
        ax.set_xticklabels([])


def __render_y_labels(pi, ax):
    if pi.x_labels:
        ax.set_yticks(np.arange(len(pi.y_labels)))
        ax.set_yticklabels(list(pi.y_labels))
    else:
        ax.set_yticklabels([])


#########################################################################################
# different plot types
#########################################################################################

#########################################################################################
# BAR PLOTS
#########################################################################################

def bar_plot(df, y, x=None, ax=None, fig=None, **kwargs):
    pi = __get_plot_info(kwargs)

    if ax is None and len(df) < 150:
        fig, ax = plt.subplots(1)
    elif ax is None:
        print("WARNING, bar plot requires scaling")
        fig, ax = plt.subplots(figsize=(len(df)*0.10, 3))

    y_data = list(df[y])
    x_data = np.arange(0, len(df))
    #if x is not None:
    #    x_data = list(df[x])

    ax.bar(x_data, y_data)

    #__render_x_labels(pi, ax)

    fig.tight_layout()

    return fig, ax


def main():
    d = {"x_labels" : [0, 1, 2]}
    pi = __get_plot_info(d)
    print(pi.x_labels)

if __name__ == "__main__":

    main()



