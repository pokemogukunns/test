from flask import Flask, jsonify, request
from flask_cors import CORS
import subprocess

app = Flask(__name__)

# CORSを設定（すべてのオリジン、GETとPOSTメソッドを許可）
CORS(app, origins='*', methods=['GET', 'POST'])

@app.route('/channel/<channelid>/<nanika>', methods=['GET', 'POST'])
def get_channel_data(channelid, nanika):
    # nanikaが空なら'videos'を使用
    if not nanika:
        nanika = 'videos'  # 'videos'という文字列を代入
        youtube_url = f'https://inv.nadeko.net/channel/{channelid}/{nanika}'  # nanikaが'videos'に設定された後にURLを生成
    else:
        youtube_url = f'https://inv.nadeko.net/channel/{channelid}/{nanika}'

    if request.method == 'GET':
        try:
            # curlでHTMLを取得
            result = subprocess.run(['curl', '-s', youtube_url], capture_output=True, text=True, check=True)
            html_content = result.stdout
        except subprocess.CalledProcessError as e:
            return jsonify({'error': 'Failed to fetch data from YouTube'}), 500
        
        return html_content

    # POSTメソッドでの処理（必要なら実装）
    elif request.method == 'POST':
        data = request.json  # JSONデータを受け取る
        return jsonify({'message': 'POST request received', 'data': data}), 200

        
#@app.route('/search', methods=['GET', 'POST'])
#def get_word_data():
 #   if request.method == 'GET':
        # クエリパラメータから検索ワードを取得
  #      word = request.args.get('q')  # 'q'を取得する

   #     if not word:
    #        return jsonify({'error': 'Search query is missing'}), 400

        # YouTubeの検索URLを生成
     #   youtube_url = f'https://www.youtube.com/results?search_query={word}'

        # curlでHTMLを取得
      #  try:
       #     result = subprocess.run(['curl', '-s', youtube_url], capture_output=True, text=True, check=True)
        #    html_content = result.stdout
        #except subprocess.CalledProcessError as e:
         #   return jsonify({'error': 'Failed to fetch data from YouTube', 'details': str(e)}), 500
        
       # return html_content

    #elif request.method == 'POST':
     #   data = request.json  # JSONデータを受け取る
      #  return jsonify({'message': 'POST request received', 'data': data}), 200


if __name__ == '__main__':
    app.run(debug=True)
