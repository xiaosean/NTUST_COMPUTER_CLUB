import pandas as pd
# pandas -> panel data

def load_xlxs():
    # 讀取xlsx data frame 並秀出資料
    df = pd.read_excel("二伯母麻花捲.xlsx")
    # print(df) 
    return df

    # skiprow 可以跳過幾前幾列
    # df = pd.read_excel("二伯母麻花捲.xlsx", skiprows = 1)
    # print(df)
def iter_col(df):
    df["total"] = 0
    for i in df.columns:
        print("i->欄位名稱 = ",i)
        print("df[i]")
        print(df[i])


def add_total(df):
    # 將nan轉為0  不然加總會為 nan 
    df = df.fillna(0)

    # 假設每包價錢不同
    price_d = {}
    # print(df.loc["原味內褲":"咖啡牛奶子"])
    # 設定每個價錢

    for index, i in enumerate(df.columns[1:]):
        print(index, i)
        price_d[i] = (index+5) * 10
    # # print(price_d)
    df["total"] = 0
    for key, value in price_d.items():
        print(key, value)
        df["total"] += df[key] * value
    # print(df)
    return df

if __name__ == '__main__':
    # 讀取xlsx data frame 並秀出資料
    df = load_xlxs()
    # print(df)

    # 列出欄位名稱
    # print(df.columns)

    # 秀出某一欄
    # print(df["黑糖"])

    
    # 對每一欄動作 
    # iter_col(df)

    df = add_total(df)

    # 最後依照某一列排序
    df = df.sort(["total"], ascending=False)
    # print(df)
    df.to_excel("處理完成的.xlsx")
