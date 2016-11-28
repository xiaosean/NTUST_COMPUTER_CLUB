import pandas as pd
import numpy as np

if __name__ == '__main__':
    df = pd.read_excel("105_eng_score.xlsx", encoding = "utf8")
    # df = pd.read_csv("tabula-1050808score.csv", encoding = "utf8")
    # print(df)
    df["分類"] = "A"
    # mask = 
    df.loc[df["總分"] < 550, "分類"] = "B"
    df.loc[df["總分"] < 350, "分類"] = "C"
    
    # df[df["總分"] < 350]["分類"] = "C"
    # df.to_excel("105_eng_score_classify.xlsx")
    
    classify_list = [df[df["分類"] == "A"].size, df[df["分類"] == "B"].size, df[df["分類"] == "C"].size]
    A_percent = df[df["分類"] == "A"].size / sum(classify_list)
    B_percent = df[df["分類"] == "B"].size / sum(classify_list)
    C_percent = df[df["分類"] == "C"].size / sum(classify_list)
    print(A_percent)
    classify_tag_list = ["A\r 550UP\r (" + str(round(A_percent*100,2 )) + "% )", "B\r 350~550\r (" + str(round(B_percent*100, 2)) + "% )", "C\r 0~350\r(" + str(round(C_percent*100, 2)) + "% )"]

    classify_dict ={"人數":classify_list, "分類": classify_tag_list}
    classify_df = pd.DataFrame(classify_dict, index = ["1", "2", "3"])
    classify_df.to_excel("105_eng_score_classify_class.xlsx")
