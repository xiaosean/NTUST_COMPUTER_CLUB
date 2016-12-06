from bokeh.charts import Donut, show, output_file
from bokeh.charts.utils import df_from_json
from bokeh.sampledata.olympics2014 import data
import pandas as pd

if __name__ == '__main__':    
    # utilize utility to make it easy to get json/dict data converted to a dataframe
    # df = df_from_json(data)
    df = pd.read_excel("105_eng_score_classify_class.xlsx", encoding = "utf8")
    # filter by countries with at least one medal and sort by total medals
    # df = df[df['total'] > 8]
    # df = df.sort("total", ascending=False)
    # df = pd.melt(df, id_vars=['abbr'],
    #              value_vars=['bronze', 'silver', 'gold'],
    #              value_name='medal_count', var_name='medal')

    # # original example
    # d = Donut(df, label=['abbr', 'medal'], values='medal_count',
    #           text_font_size='8pt', hover_text='medal_count')
    # print(df[df["分類"] == "A"].size)
    # print(df[df["分類"] == "B"].size)
    # print(df[df["分類"] == "C"].size)
    # classify_list = [df[df["分類"] == "A"].size, df[df["分類"] == "B"].size, df[df["分類"] == "C"].size]
    # classify_tag_list = ["A", "B", "C"]
    # classify_df = pandas(dict(zip(classify_tag_list, classify_list)))
    d = Donut(df, label="分類", values="人數",
              text_font_size='14pt', color = ["#EBD4CB", "#EEEFA8", "#92DCE5"])

    output_file("donut.html", title="donut.py example")

    show(d)