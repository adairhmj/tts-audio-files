from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/api/hello', methods=['POST'])
def hello():
    data = request.get_json()
    name = data.get('name', 'World')
    return jsonify({"greeting": f"Hello, {name}!"})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "OK"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))  # 优先使用环境变量，否则默认 8000
    app.run(host='0.0.0.0', port=port)
