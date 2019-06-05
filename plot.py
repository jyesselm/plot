#!/usr/bin/env python

import argparse
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import gridspec

import grid_strategy


sns.set_style("white")
sns.set_context("talk")
sns.set_style("ticks")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-csv', help='dataframe in csv format', required=True)
    parser.add_argument('-t', help='type', required=True)
    parser.add_argument('-vars', help='variables')
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


def dist_all_plot(df):
    pass


def main():
    args = parse_args()
    df = pd.read_csv(args.csv)

    if args.t == 'dist':
        sns.distplot(df[args.vars])

    if args.t == 'distall':
        fig = plt.figure()
        cols = get_number_columns(df)
        grid_arrangement = grid_strategy.GridStrategy.get_grid(len(cols))
        gs = grid_strategy.get_gridspec(grid_arrangement)
        for i, c in enumerate(cols):
            ax = fig.add_subplot(gs[i])
            sns.distplot(df[cols[i]], ax=ax)
            adjust_axis_to_be_square(ax)
            despine_axis(ax)

    plt.show()




if __name__ == "__main__":
    main()
