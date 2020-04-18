import pandas as pd
from bokeh.plotting import figure, output_file, show, save
from bokeh.models import ColumnDataSource
from bokeh.models.ranges import FactorRange
from bokeh.sampledata.iris import flowers
from bokeh.models import HoverTool, LabelSet, FixedTicker


def __map_labels_correctly(p, num_bars, x_labels):
    pass


def bar_plot(bars, x_labels=None, plot_height=250):
    p = figure(x_range=(-1, len(bars)+1), plot_height=plot_height, toolbar_location=None, tools="")

    if x_labels is not None:
        __map_labels_correctly(p, len(bars), x_labels)
