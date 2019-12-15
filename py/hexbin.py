import numpy as np

from bokeh.io import output_file, show
from bokeh.models import HoverTool
from bokeh.plotting import figure, curdoc
from bokeh.transform import factor_cmap
from bokeh.themes import built_in_themes
from bokeh.palettes import Greys256
from bokeh.embed import components

ppal = ['#dddddd']

n = 500
x = 2 + 2*np.random.standard_normal(n)
y = 2 + 2*np.random.standard_normal(n)
curdoc().theme = 'light_minimal'
p = figure(title="LG//2019. テクニカルディレクター", match_aspect=True,
           tools="", background_fill_color='#ffffff',plot_width=1280,plot_height=720)
p.grid.visible = False

for uuu in dir(p):
    print(uuu)

r, bins = p.hexbin(x,
                    y,
                    size=1,
                    hover_color="#bbbbbb",
                    hover_alpha=0.2,
                    palette=ppal,
                    line_color='#cccccc')

p.circle(x, y, color="white", size=1)
#("count", "@c"), ("(q,r)", "(@q, @r)")
p.add_tools(HoverTool(
    tooltips=None,
    mode="mouse", point_policy="follow_mouse", renderers=[r]
))

output_file("hexbin.html")

show(p)