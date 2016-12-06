import pandas as pd
from bokeh.charts import Bar, output_file, show
from bokeh.charts.attributes import ColorAttr, CatAttr
from bokeh.models import Range1d
df = pd.read_excel("105_score_sort_filter_500.xlsx")

# # prepare some data
# score_list = [x for x in df["普通生\r錄取分數"]]
# score_list = score_list[:5]
# data = {"y": score_list}
# print(data)
# # output to static HTML file

# df = zip([x for x in df["普通生\r錄取分數"]], [y for y in df["校名"]])
# df = df.sort(["普通生\r錄取分數"], ascending = [0])
# print(df["校系名"])
# print(df["普通生\r錄取分數"])
# label = CatAttr(columns=['校系名'], sort=False) 否則會照著字的utf-8的編碼排序
y_start, y_end = (480, 660)
ydr = Range1d(y_start, y_end)

p = Bar(df, values='普通生\r錄取分數', label = CatAttr(columns=['校系名'], sort=False), title="學校系所分數高低", bar_width=0.4, agg='min' ,legend=False, y_range = ydr, color = "color")
# transpose(p)

# p.toolbar_location = None
p.logo = None

output_file("bar.html")

show(p)

# # show the results
# show(p)

