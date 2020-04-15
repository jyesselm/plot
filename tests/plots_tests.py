import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import unittest
import uuid

from fplot.plots import *

sns.set_style("white")
sns.set_context("talk")


class Unittest(unittest.TestCase):

    def test_bar_plot(self):
        self.skipTest("all works for now")

        # basic test
        df_a = sns.load_dataset("anscombe")
        df_t = sns.load_dataset("tips")

        fig, ax = bar_plot(df_a["x"])
        fig.savefig("outputted_plots/bar_plot_1.pdf")

        # smaller number of bars
        fig, ax = bar_plot(df_a["x"][:4])
        fig.savefig("outputted_plots/bar_plot_2.pdf")

        # larger number of bars
        fig, ax = bar_plot(df_t["total_bill"])
        fig.savefig("outputted_plots/bar_plot_3.pdf")

        pal = sns.color_palette('deep')

        # test specifying axis and figure instead of allowing the function to make it
        fig, axs = plt.subplots(3)
        bar_plot(df_a["x"], ax=axs[0], fig=fig, color=pal[0])
        bar_plot(df_a["x"][:4], ax=axs[1], fig=fig, color=pal[1])
        bar_plot(df_t["total_bill"], ax=axs[2], fig=fig, color=pal[2])
        fig.savefig("outputted_plots/bar_plot_4.pdf")

    def test_bar_plot_labels(self):
        self.skipTest("all works for now")

        df_a = sns.load_dataset("anscombe")
        df_t = sns.load_dataset("tips")

        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        labels = []
        c = 0
        for i in range(0, 100):
            labels.append(chars[c] * 10)
            c += 1
            if c == len(chars):
                c = 0

        # add labels
        fig, ax = bar_plot(df_t["total_bill"],
                           x_labels="A" * len(df_t["total_bill"]))
        fig.savefig("outputted_plots/bar_plot_5.pdf")

        long_labels = [str(uuid.uuid1()) for x in range(0, len(df_t))]
        fig, ax = bar_plot(df_t["total_bill"][0:10],
                           x_labels=long_labels[0:10])
        fig.savefig("outputted_plots/bar_plot_6.pdf")


        fig, ax = bar_plot(df_t["total_bill"][0:2], x_labels=labels[0:2])
        fig.savefig("outputted_plots/bar_plot_7.pdf")

        fig, ax = bar_plot(df_t["total_bill"][0:50],
                           x_labels="A" * len(df_t["total_bill"][0:50]))
        fig.savefig("outputted_plots/bar_plot_8.pdf")

        df = pd.concat([df_t, df_t])

        fig, ax = bar_plot(df["total_bill"],
                           x_labels="A" * len(df))
        fig.savefig("outputted_plots/bar_plot_9.pdf")

        pal = sns.color_palette('deep')

        # test specifying axis and figure instead of allowing the function to make it
        fig, axs = plt.subplots(3, figsize=(6.4, 10))
        bar_plot(df_a["x"][0:3], ax=axs[0], fig=fig, color=pal[0], x_labels="A,B,C".split(","))
        bar_plot(df_a["x"], ax=axs[1], fig=fig, color=pal[1], x_labels=labels[0:len(df_a)])
        bar_plot(df_t["total_bill"], ax=axs[2], fig=fig, color=pal[2])
        fig.tight_layout()
        fig.savefig("outputted_plots/bar_plot_10.pdf")

        #fig, ax = plt.subplots(1)
        #print(fig.get_size_inches())
        #exit()


        #ax.bar(np.arange(0, 5), df_t["total_bill"][0:5])
        #ax.set_xticks(np.arange(0, 5))
        #ax.set_xticklabels(shorter_labels[0:5])
        #fig.savefig("test.pdf")

    def test_group_bar_plot(self):
        df = sns.load_dataset("anscombe")
        #df = df[0:10]
        fig, ax = group_bar_plot(df, ["x", "y"], df["dataset"])
        fig.legend()
        fig.savefig("outputted_plots/group_bar_plot_1.pdf")

        #df["z"] = df["x"]*0.25 + df["y"]



    def _test_really_big_bar_plot(self):
        df = pd.read_csv("../data/helical_variation_final.csv")
        fig, ax = bar_plot(df["dG"])
        fig.savefig("outputted_plots/bar_plot_6.pdf")

        #df = df[:100]
        #fig, ax = plt.subplots(1)
        #g = sns.barplot(np.linspace(0, 10, len(df)), df["dG"], ax=ax)
        #fig.savefig("outputted_plots/bar_plot_7.pdf")




def main():
    unittest.main()

if __name__ == '__main__':
    main()