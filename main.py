from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# CORSを設定（すべてのオリジン、GETとPOSTメソッドを許可）
CORS(app, origins='*', methods=['GET', 'POST'])

@app.route('/channel/<channelid>', methods=['GET', 'POST'])
def get_channel_data(channelid):
    # GETメソッドでの処理
    if request.method == 'GET':
        # YouTubeのURLを生成
        youtube_url = f'https://www.youtube.com/channel/{channelid}'

        # curlでHTMLを取得
        try:
            result = subprocess.run(['curl', '-s', youtube_url], capture_output=True, text=True, check=True)
            html_content = result.stdout
        except subprocess.CalledProcessError as e:
            return jsonify({'error': 'Failed to fetch data from YouTube'}), 500
        
        return html_content

    # POSTメソッドでの処理（必要なら実装）
    elif request.method == 'POST':
        data = request.json  # 例えばJSONデータを受け取る
        return jsonify({'message': 'POST request received', 'data': data}), 200
        
@app.route('/search?q=<waod>', methods=['GET', 'POST'])
def get_word_data(word):
    # GETメソッドでの処理
    if request.method == 'GET':
        # YouTubeのURLを生成
        youtube_url = f'https://www.youtube.com/search?q={word}'

        # curlでHTMLを取得
        try:
            result = subprocess.run(['curl', '-s', youtube_url], capture_output=True, text=True, check=True)
            html_content = result.stdout
        except subprocess.CalledProcessError as e:
            return jsonify({'error': 'Failed to fetch data from YouTube'}), 500
        
        return html_content

    # POSTメソッドでの処理（必要なら実装）
    elif request.method == 'POST':
        data = request.json  # 例えばJSONデータを受け取る
        return jsonify({'message': 'POST request received', 'data': data}), 200


if __name__ == '__main__':
    app.run(debug=True)
