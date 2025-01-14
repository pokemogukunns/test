import subprocess
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/channel/<channelid>', methods=['GET'])
def get_channel_data(channelid):
    # YouTubeのURLを生成
    youtube_url = f'https://www.youtube.com/channel/{channelid}'

    # curlコマンドを実行してURLのレスポンスを取得
    try:
        result = subprocess.run(['curl', '-s', youtube_url], capture_output=True, text=True, check=True)
        response_text = result.stdout
    except subprocess.CalledProcessError as e:
        return jsonify({'error': 'Failed to fetch data from YouTube'}), 500

    # 取得したテキストをそのまま返す
    return response_text

if __name__ == '__main__':
    app.run(debug=True)
