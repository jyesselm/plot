import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import unittest

from fplot.plots import *

sns.set_style("white")
sns.set_context("talk")


class Unittest(unittest.TestCase):

    def test_bar_plot(self):
        df = sns.load_dataset("anscombe")
        fig, ax = bar_plot(df, "x")
        fig.savefig("outputted_plots/bar_plot_1.png", dpi=100)
        plt.clf()

        df = sns.load_dataset("tips")
        fig, ax = bar_plot(df, "total_bill")
        fig.savefig("outputted_plots/bar_plot_2.png", dpi=100)

    def _test_really_big_bar_plot(self):
        df = pd.read_csv("../data/helical_variation_final.csv")
        fig, ax = bar_plot(df, "dG")
        fig.savefig("outputted_plots/bar_plot_3.png", dpi=50)




def main():
    unittest.main()

if __name__ == '__main__':
    main()