#!/usr/bin/env python

import argparse
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_style("white")
sns.set_context("talk")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-csv', help='dataframe in csv format', required=True)
    parser.add_argument('-t', help='type', required=True)
    parser.add_argument('-vars', help='variables')
    args = parser.parse_args()
    return args


#########################################################################################
# helper functions
#########################################################################################

def get_number_columns(df):
    cols = []
    col_names = df.columns
    for i, dtype in enumerate(df.dtypes):
        if dtype == "float64":
            cols.append(col_names[i])
    return cols


#########################################################################################
# single axis plots
#########################################################################################

def dist_plot(df, ax):
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
        cols = get_number_columns(df)
        fig, axes = plt.subplots(nrows=1, ncols=2)
        for i, ax in enumerate(axes):
            sns.distplot(df[cols[i]], ax=ax)


    plt.show()




if __name__ == "__main__":
    main()
