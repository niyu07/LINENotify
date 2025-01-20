from dotenv import load_dotenv
import os
import requests

load_dotenv()
# .envファイルにTOKENを書いてください
token = os.getenv("LINE_TOKEN")
# LINE Notifyのアクセストークンを定義
LINE_token = token  # アクセストークンに置き換えてください
image_path = "YOUR_IMAGEPATH"
# LINEメッセージ送信の関数
def LINE_message(msg):
    # APIエンドポイントのURLを定義
    url = "https://notify-api.line.me/api/notify"
    
    # HTTPリクエストヘッダーの設定
    headers = {"Authorization": "Bearer " + LINE_token}
    
    # 送信するメッセージの設定
    payload = {"message": msg}
    
    # 送信する画像の設定
    files = {"imageFile": open(image_path, "rb")}
    
    # POSTリクエストの送信
    r = requests.post(url, headers=headers, data=payload, files=files)
    
    # ファイルを閉じる
    files["imageFile"].close()

# 最新のディレクトリを取り出し，ファイルの中身を送信する
def find_latest_file():
    # logディレクトリ内のファイルを取得
    logs = os.listdir('./log')
    #　後で調べる
    dirs = [d for d in logs if os.path.isdir(os.path.join('./log', d))]
    # 最も新しいディレクトリを選択
    latest_dir = max(dirs, key=lambda d: os.path.getmtime(os.path.join('./log', d)))
    
    # 最新のディレクトリ内のdevice_info.txtを指定
    log_path = os.path.join('./log', latest_dir, 'device_info.txt')
    print(log_path)
    # ファイルの中身を送信
    with open(log_path, 'r') as f:
        content = f.read() 
    linemsg = f"\n {latest_dir} \n {content}"
    print(content)
    LINE_message(linemsg)
# 関数の呼び出し
find_latest_file()
