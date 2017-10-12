from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure
import pandas as pd
import numpy as np

df = pd.read_csv('test.csv')
output_file("Bug_Bar.html")

RdYlGn6 = ["#1a9850", "#91cf60", "#d9ef8b", "#fee08b", "#fc8d59", "#d73027"]
names = df['NAME'].tolist()
stat = ["HP","ATTACK","DEFENSE","SP_ATTACK","SP_DEFENSE","SPEED"]
statname = ['Hit Points','Attack','Defense','Sp. Attack','Sp. Defense','Speed']


hover = HoverTool(tooltips=[
    ("Name", "@NAME"),
    ("Attack", "@ATTACK"),
    ("Defense", "@DEFENSE"),
    ("HP","@HP"),
    ("Speed","@SPEED"),
    ("Sp. Attack", "@SP_ATTACK"),
    ("Sp. Defense", "@SP_DEFENSE")
])

p = figure(y_range=np.sort(names).tolist(), plot_height=1000, x_range=(0, 700), title="Bug Type Base Stats",
           toolbar_location=None)

p.hbar_stack(stat, y='NAME', height=0.9, color=RdYlGn6, source=ColumnDataSource(df),legend=["%s" % x for x in statname],hover_line_color="black",hover_fill_color=RdYlGn6)

p.add_tools(hover)


p.y_range.range_padding = 0.1
p.ygrid.grid_line_color = None
p.legend.location = "bottom_right"
p.axis.minor_tick_line_color = None
p.outline_line_color = None

show(p)