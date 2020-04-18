import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import unittest
import uuid

from fplot.plots import *

sns.set_style("white")
sns.set_context("talk")


class Counter(object):
    def __init__(self):
        self.count = -1

    def get_count(self):
        self.count += 1
        return self.count


def _render_figure_to_pdf(fig, name, counter):
    fig.savefig("outputted_plots/"+name+"_"+str(counter.get_count())+".pdf")

class Unittest(unittest.TestCase):

    def test_bar_plot(self):
        self.skipTest("all works for now")

        counter = Counter()
        name = "test_bar_plot"
        # basic test
        df_a = sns.load_dataset("anscombe")
        df_t = sns.load_dataset("tips")

        fig, ax = bar_plot(df_a["x"])
        _render_figure_to_pdf(fig, name, counter)

        # smaller number of bars
        fig, ax = bar_plot(df_a["x"][:4])
        _render_figure_to_pdf(fig, name, counter)

        # larger number of bars
        fig, ax = bar_plot(df_t["total_bill"])
        _render_figure_to_pdf(fig, name, counter)

        pal = sns.color_palette('deep')

        # test specifying axis and figure instead of allowing the function to make it
        fig, axs = plt.subplots(3)
        bar_plot(df_a["x"], ax=axs[0], fig=fig, color=pal[0])
        bar_plot(df_a["x"][:4], ax=axs[1], fig=fig, color=pal[1])
        bar_plot(df_t["total_bill"], ax=axs[2], fig=fig, color=pal[2])
        _render_figure_to_pdf(fig, name, counter)

        # using set of colors instead of a single color
        fig, ax = bar_plot(df_a["x"][0:10], color=pal)
        _render_figure_to_pdf(fig, name, counter)

        fig, ax = bar_plot(df_a["x"][0:20], color=pal)
        _render_figure_to_pdf(fig, name, counter)

        fig, ax = bar_plot(df_a["x"][0:2], color=pal)
        _render_figure_to_pdf(fig, name, counter)


    def test_bar_plot_labels(self):
        self.skipTest("all works for now")
        counter = Counter()
        name = "test_bar_plot_labels"

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
        _render_figure_to_pdf(fig, name, counter)

        long_labels = [str(uuid.uuid1()) for x in range(0, len(df_t))]
        fig, ax = bar_plot(df_t["total_bill"][0:10],
                           x_labels=long_labels[0:10])
        _render_figure_to_pdf(fig, name, counter)


        fig, ax = bar_plot(df_t["total_bill"][0:2], x_labels=labels[0:2])
        _render_figure_to_pdf(fig, name, counter)

        fig, ax = bar_plot(df_t["total_bill"][0:50],
                           x_labels="A" * len(df_t["total_bill"][0:50]))
        _render_figure_to_pdf(fig, name, counter)

        df = pd.concat([df_t, df_t])

        fig, ax = bar_plot(df["total_bill"],
                           x_labels="A" * len(df))
        _render_figure_to_pdf(fig, name, counter)

        pal = sns.color_palette('deep')

        # test specifying axis and figure instead of allowing the function to make it
        fig, axs = plt.subplots(3, figsize=(6.4, 10))
        bar_plot(df_a["x"][0:3], ax=axs[0], fig=fig, color=pal[0], x_labels="A,B,C".split(","))
        bar_plot(df_a["x"], ax=axs[1], fig=fig, color=pal[1], x_labels=labels[0:len(df_a)])
        bar_plot(df_t["total_bill"], ax=axs[2], fig=fig, color=pal[2])
        fig.tight_layout()
        _render_figure_to_pdf(fig, name, counter)

        #fig, ax = plt.subplots(1)
        #print(fig.get_size_inches())
        #exit()


        #ax.bar(np.arange(0, 5), df_t["total_bill"][0:5])
        #ax.set_xticks(np.arange(0, 5))
        #ax.set_xticklabels(shorter_labels[0:5])
        #fig.savefig("test.pdf")


    def test_group_bar_plot(self):
        self.skipTest("all works for now")
        counter = Counter()
        name = "test_group_bar_plot"

        df = sns.load_dataset("anscombe")
        fig, ax = group_bar_plot(df, ["x", "y"], df["dataset"])
        fig.legend()
        _render_figure_to_pdf(fig, name, counter)

        df["z"] = df["x"]*0.25 + df["y"]
        df["a"] = df["y"] * 0.25 + df["x"]

        fig, ax = group_bar_plot(df, ["x", "y", "z", "a"], df["dataset"])
        fig.legend()
        _render_figure_to_pdf(fig, name, counter)

        fig, ax = group_bar_plot(df, ["x", "y", "z", "a"], df["dataset"])
        fig.legend()
        _render_figure_to_pdf(fig, name, counter)


    def test_stacked_bar_plot(self):
        #self.skipTest("all works for now")
        counter = Counter()
        name = "test_stacked_bar_plot"
        df = pd.DataFrame(columns="A,B".split(","))
        df["A"] = range(0, 125, 25)
        df["B"] = range(0, 125, 25)[::-1]

        fig, ax = stacked_bar_plot(df, ["A", "B"])
        _render_figure_to_pdf(fig, name, counter)

        df = pd.DataFrame(columns="A,B".split(","))
        df["A"] = range(0, 125, 1)
        df["B"] = range(0, 125, 1)[::-1]

        fig, ax = stacked_bar_plot(df, ["A", "B"])
        _render_figure_to_pdf(fig, name, counter)

        flatui = ["#9b59b6", "#3498db"]
        pal = sns.color_palette(flatui)
        fig, ax = stacked_bar_plot(df, ["A", "B"], pal=pal)
        _render_figure_to_pdf(fig, name, counter)






    def test_color_palettes(self):
        self.skipTest("all works for now")

        counter = Counter()
        name = "test_color_palettes"

        pal = sns.light_palette("purple")
        fig, ax = palplot(pal)
        _render_figure_to_pdf(fig, name, counter)

        pal = sns.light_palette("purple", 20)
        fig, ax = palplot(pal)
        _render_figure_to_pdf(fig, name, counter)

        flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
        fig, ax = palplot(sns.color_palette(flatui))
        _render_figure_to_pdf(fig, name, counter)

        flatui = ["yellow", "red", "green", "blue"]
        fig, ax = palplot(sns.color_palette(flatui))
        _render_figure_to_pdf(fig, name, counter)

        colors = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
        fig, ax =  palplot(sns.xkcd_palette(colors))
        _render_figure_to_pdf(fig, name, counter)



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