import argparse
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import math
import matplotlib.textpath as textpath
from matplotlib import gridspec
from collections import namedtuple

sns.set_style("white")
sns.set_context("talk")
sns.set_style("ticks")


def __get_plot_kwargs(kwargs):
    valid = "title,color,width".split(",")

    plot_kwargs = {}
    for k, v in kwargs.items():
        if k in valid:
            plot_kwargs[k] = v
    return plot_kwargs


def __get_avg_char_length():
    all_chars = "abcdefghijklmnopqrstuvwxyz0123456790"
    avg_len = {}
    for i in np.arange(0.2, 14, 0.1):
        i = round(i, 1)
        t = textpath.TextPath((0, 0), all_chars, size=i)
        contents = t.get_extents()
        act_width = contents.x1 - contents.x0
        avg_len[i] = act_width / len(all_chars)
    return avg_len


def __find_ideal_font_size(line, size):
    best_size = 12.0
    avg_lengths = __get_avg_char_length()
    act_width = avg_lengths[best_size]*len(line)
    while act_width > size:
        best_size = round(best_size-0.1, 1)
        act_width = avg_lengths[best_size] * len(line)
        if best_size < 3.0:
            break
    return (best_size-0.1)


def __get_fig_size_by_data(num_points, x_labels, cols):
    #initial_figsize = [6.4, 4.8] # default matplotlib ratio
    scale_size = num_points * cols * 0.14
    if x_labels is None:
        if scale_size < 6.4:
            return (6.4, 4.8)
        else:
            return (scale_size, 4.8)

    else:
        if scale_size < 6.4:
            return (6.4, 4.8)
        else:
            return (scale_size, 4.8)



#########################################################################################
# different plot types
#########################################################################################

def __bar_plot(x, y, ax, **kwargs):
    ax.bar(x, y, **kwargs)

#########################################################################################
# BAR PLOTS
#########################################################################################

def bar_plot(bars, x_labels=None, ax=None, fig=None, **kwargs):
    width = 1
    spacing = width * 1.10
    ax_is_none = 0
    x_data = []

    fig_size = __get_fig_size_by_data(len(bars), x_labels, 1)

    if ax is None:
        ax_is_none = 1
        fig, ax = plt.subplots(figsize=fig_size, dpi=300)
        x_data = np.linspace(0, len(bars)*width*1.10, len(bars))
    else:
        x_lim = ax.get_xlim()
        x_data = np.linspace(x_lim[0], x_lim[1], len(bars))
        width = (x_data[0]-x_data[1])*0.90

    plot_kwargs = __get_plot_kwargs(kwargs)
    plot_kwargs["width"] = width

    # TODO should not hardcode this
    plot_kwargs["linewidth"] = 0

    if not "color" in plot_kwargs:
        plot_kwargs["color"] = '#4c72b0'

    __bar_plot(x_data, bars, ax, **plot_kwargs)

    # for bar plots having default ticks make no sense, just remove them
    if ax_is_none:
        # TODO need some more complex scaling for small number of bars with default figsize
        ax.set_xlim([x_data[0]-width*1.5, x_data[-1]+width*1.5])

    wont_fit = 0
    if x_labels is not None:
        label_length = "".join(x_labels)
        max_length = (fig_size[0] * 0.9) * 60  # 35 is a random scale
        ideal_size_horizontal = __find_ideal_font_size(label_length, max_length)

        if fig_size[0] < 6.5 and ideal_size_horizontal > 3:
            ideal_size_horizontal = 14
        elif fig_size[0] < 6.5 and len(bars) < 12:
            ideal_size_horizontal = 12
            wont_fit = 1

        if ideal_size_horizontal < 3.0:
            wont_fit = 1
            ideal_size_horizontal = 6.0
        if ideal_size_horizontal < 3.0:
            ideal_size_horizontal = 3.0
            print("WARNING text is going to be squished")
        ax.set_xticks(x_data)

        if wont_fit:
            ax.set_xticklabels(x_labels, fontdict={'fontsize': 6}, rotation=90)
        else:
            ax.set_xticklabels(x_labels, fontdict={'fontsize': ideal_size_horizontal})
    else:
        ax.set_xticks([])


    if ax_is_none:
        ax.set_xlim([x_data[0]-width*1.5, x_data[-1]+width*1.5])
        fig.tight_layout()

    return fig, ax


def group_bar_plot(df, cols, x_labels, col_labels=None, ax=None, fig=None, **kwargs):
    fig_size = __get_fig_size_by_data(len(df), x_labels, 1)
    width = 1
    ax_is_none = 0

    if ax is None:
        ax_is_none = 1
        fig, ax = plt.subplots(figsize=fig_size, dpi=300)
        x_data = np.linspace(0, width*len(df)*(len(cols)+1), len(df)*(len(cols)+1))
    else:
        x_lim = ax.get_xlim()
        x_data = np.linspace(x_lim[0], x_lim[1], len(df))
        width = (x_data[0] - x_data[1]) * 0.90

    bars = []
    for c in cols:
        bars.append(list(df[c]))

    rs = [[] for x in range(len(cols)+1)]
    count = 0
    for i in range(len(x_data)):
        rs[count].append(x_data[i])
        count += 1
        if count > len(cols):
            count = 0

    if col_labels is None:
        col_labels = cols

    for i in range(len(bars)):
        ax.bar(rs[i], bars[i], width=width, linewidth=0, label=col_labels[i])

    #ax.set_xticks([r + width for r in range(len(bars[0]))])
    #ax.set_xticklabels(x_labels)
    ax.set_xticks([])

    if ax_is_none:
        #ax.set_xlim([x_data[0] - width * 1.5, x_data[-1] + width * 1.5])
        fig.tight_layout()

    return fig, ax


def main():
    pass

if __name__ == "__main__":

    main()



