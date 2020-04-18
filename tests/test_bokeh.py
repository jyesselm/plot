import unittest
import seaborn as sns
import pandas as pd
from bokeh.plotting import figure, output_file, show, save
from bokeh.models import ColumnDataSource
from bokeh.models.ranges import FactorRange
from bokeh.sampledata.iris import flowers
from bokeh.models import HoverTool, LabelSet, FixedTicker

class Counter(object):
    def __init__(self):
        self.count = -1

    def get_count(self):
        self.count += 1
        return self.count


def _render_figure(p, name, counter):
    output_file(filename="outputed_plots_bokeh/"+name+"_"+str(counter.get_count())+".html", title="test")
    save(p)

class BokehPlottingTests(unittest.TestCase):

    def test_bar_plots(self):
        counter = Counter()
        name = "test_bar_plot"
        # basic test
        df_a = sns.load_dataset("anscombe")
        df_t = sns.load_dataset("tips")
        df_a["num"] = [str(x) for x in range(0, len(df_a))]

        with self.subTest("test basic barplot"):
            p = figure(x_range=(-1, 44), plot_height=250, title="test x plot",
                    toolbar_location=None, tools="")

            overrides = { i : row["dataset"] for i, row in df_a.iterrows() }
            overrides[-1] = ""
            overrides[44] = ""

            p.vbar(x=range(0, 44), top=df_a["x"], width=0.5)
            p.xaxis.ticker.desired_num_ticks = 44
            p.xaxis.major_label_overrides = overrides
            p.xaxis.minor_tick_line_color = None
            p.xgrid.grid_line_color = None
            p.y_range.start = 0

            show(p)
            _render_figure(p, name, counter)


        """with self.subTest("test changing colors"):
            p = figure(x_range=df_a["num"], plot_height=250, title="test x plot",
                    toolbar_location=None, tools="")

            p.vbar(x=df_a["num"], top=df_a["x"], width=0.5)
            p.xgrid.grid_line_color = None
            p.y_range.start = 0
            _render_figure(p, name, counter)"""

def main():
    unittest.main()

if __name__ == '__main__':
    main()



"""colormap = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
colors = [colormap[x] for x in flowers['species']]

p = figure(title = "Iris Morphology")
p.xaxis.axis_label = 'Petal Length'
p.yaxis.axis_label = 'Petal Width'


source = ColumnDataSource(dict(
    x=flowers["petal_length"],
    y=flowers["petal_width"],
    color=colors,
    label=range(0, len(flowers))
))

p.circle( x='x', y='y', color='color', source=source, size=10)


p.add_tools(HoverTool(
    tooltips=[("(petal_length,petal_width,label)", "(@x, @y, @label)")],
    mode="mouse", point_policy="follow_mouse"))

output_file("outputed_plots_bokeh/iris.html", title="iris.py example")



#show(p)"""