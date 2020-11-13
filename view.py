import eel
import desktop
import search

# htmlファイルのディレクトリ
app_name="html"
# htmlファイル名
end_point="index.html"
# ウィンドウのサイズ
size=(700,600)

### 課題4：ログ表示領域にkimetsu_searchの結果を出力
### 課題6：CSV保存先をHTML画面から指定可能にする
# JavaScriptから実行
@ eel.expose
def kimetsu_search(word, csv):
    # 検索処理呼び出し、結果リストに格納
    result = search.kimetsu_search(word, csv)
    # 検索結果出力処理呼び出し(JavaScript)
    eel.view_log_js(result)
    
# 画面生成処理呼び出し
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)
