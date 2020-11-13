import pandas as pd
import eel

### デスクトップアプリ作成課題
### 課題6：CSV保存先をHTML画面から指定可能にする
def kimetsu_search(word, csv):
    # 検索対象取得
    df=pd.read_csv("./" + csv)
    source=list(df["name"])
    # 検索結果
    result = ""
    # 検索
    if word in source:
        result = "『{}』はあります".format(word)
    else:
        result = "『{}』はありません".format(word)
        # 追加
        #add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        #if add_flg=="1":
        source.append(word)
    
    # 検索結果をコンソールに出力
    print(result)
    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    df.to_csv("./" + csv,encoding="utf_8-sig")
    print(source)
    # 検索結果を返却
    return result
