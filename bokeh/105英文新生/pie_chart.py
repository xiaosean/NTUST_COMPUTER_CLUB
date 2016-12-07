# 透過pandas解析excel
import pandas as pd
# 看要畫出甚麼樣的圖表 再import所需的libary
from bokeh.charts import Donut, show, output_file
from bokeh.charts.utils import df_from_json
# 程式進入點
if __name__ == '__main__':    
    # 讀取excel 
    df = pd.read_excel("105_eng_score_classify_class.xlsx", encoding = "utf8")
    # 繪製圖表 透過df的columns名稱 丟入label以及values 當作圖表的x,y軸的資料
    d = Donut(df, label="分類", values="人數",
              text_font_size='14pt', color = ["#EBD4CB", "#EEEFA8", "#92DCE5"])
    # 輸出檔案 叫做dount.html 這也是特色 可以將圖表轉為html
    output_file("donut.html", title="donut.py example")
    # 開啟瀏覽器繪圖
    show(d)