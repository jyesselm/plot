#!/usr/bin/env python

import argparse
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import gridspec
from collections import namedtuple

import grid_strategy

sns.set_style("white")
sns.set_context("talk")
sns.set_style("ticks")

class PlotGrid(object):
    def __init__(self):
        self._fig = None
        self._axes = []

    def setup(self):
        pass

    def get_next_axis(self):
        pass

class DefaultPlotGrid(PlotGrid):
    def __init__(self):
        super(DefaultPlotGrid, self).__init__()
        self._gs = None
        self._pos = 0

    def setup(self, n_plots):
        self._fig = plt.figure()
        grid_arrangement = grid_strategy.GridStrategy.get_grid(n_plots)
        self._gs = grid_strategy.get_gridspec(grid_arrangement)

    def get_next_axis(self):
        ax = self._fig.add_subplot(self._gs[self._pos])
        self._pos += 1
        self._axes.append(ax)
        return ax

class LinearPlotGrid(PlotGrid):
    def __init__(self):
        super(LinearPlotGrid, self).__init__()
        self._gs = None
        self._pos = 0

    def setup(self, n_plots):
        self._fig, self._axes = plt.subplots(1, n_plots)

    def get_next_axis(self):
        self._pos += 1
        return self._axes[self._pos - 1]

def get_plot_grid(grid_type):
    if    grid_type == "Default":
        return DefaultPlotGrid()
    elif  grid_type == "Linear":
        return LinearPlotGrid()
    else:
        raise ValueError("unknown grid type")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-csv', help='dataframe in csv format', required=True)
    parser.add_argument('-t', help='type', required=True)
    parser.add_argument('-vars', help='variables')
    parser.add_argument('-o', default=None, help='output path')
    parser.add_argument('-gt', default="Default", help="grid type")
    args = parser.parse_args()
    return args


#########################################################################################
# dataframe processing functions
#########################################################################################

def get_number_columns(df):
    cols = []
    col_names = df.columns
    for i, dtype in enumerate(df.dtypes):
        if dtype == "float64":
            cols.append(col_names[i])
        if dtype == "int64":
            cols.append(col_names[i])
    return cols


#########################################################################################
# style functions
#########################################################################################

def adjust_axis_to_be_square(ax):
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()
    ax.set_aspect((x1 - x0) / (y1 - y0))


def despine_axis(ax):
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)


#########################################################################################
# grid helpers
#########################################################################################

def get_grid_indices(nrows, ncols):
    indices = []
    Index = namedtuple('Index', ['i', 'j'])
    for i in range(ncols):
        for j in range(nrows):
            indices.append(Index(i, j))
    return indices


#########################################################################################
# single axis plots
#########################################################################################

def dist_plot(df, ax):
    pass


def heatmap(df, ax):
    pass


def lineplot(df, ax):
    pass


def scatter(df, ax):
    pass


#########################################################################################
# full figure plots
#########################################################################################


def dist_all_plot(df, plot_grid):
    cols = get_number_columns(df)
    plot_grid.setup(len(cols))
    for i, c in enumerate(cols):
        ax = plot_grid.get_next_axis()
        sns.distplot(df[cols[i]], ax=ax)
        adjust_axis_to_be_square(ax)
        despine_axis(ax)

def line_all_plot(df, plot_grid):
    cols = get_number_columns(df)
    plot_grid.setup(len(cols))
    for i, c in enumerate(cols):
        ax = plot_grid.get_next_axis()
        ax.plot(range(0, len(df)), df[c])
        adjust_axis_to_be_square(ax)
        despine_axis(ax)

def main():
    args = parse_args()
    df = pd.read_csv(args.csv)
    plot_grid = get_plot_grid(args.gt)

    if args.t == 'dist':
        sns.distplot(df[args.vars])

    if args.t == 'distall':
        dist_all_plot(df, plot_grid)

    if args.t == 'lineall':
        line_all_plot(df, plot_grid)

    #if args.t == 'scatter':
    #    vars =


    if args.t == 'scatterall':
        g = sns.PairGrid(df)
        g = g.map(plt.scatter)

        #fig.tight_layout()




    if args.o is not None:
        plt.savefig(args.o)
    else:
        plt.show()




if __name__ == "__main__":
    main()





"""

    if args.t == 'distall2':
        cols = get_number_columns(df)
        size = 2.5
        aspect = 1
        ncols = 2
        nrows = 2
        figsize = ncols * size * aspect, nrows * size
        fig, axes = plt.subplots(nrows, ncols)
        inds = get_grid_indices(ncols, nrows)
        for i, c in enumerate(cols):
            sns.distplot(df[cols[i]], ax=axes[inds[i].i, inds[i].j])
            adjust_axis_to_be_square(axes[inds[i].i, inds[i].j])
            despine_axis(axes[inds[i].i, inds[i].j])

        for i in range(len(cols), len(inds)):
            axes[inds[i].i, inds[i].j].axis('off')
"""











