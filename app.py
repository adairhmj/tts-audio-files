from flask import Flask, request, jsonify
from flask_cors import CORS
from gradio_client import Client, handle_file
import os

app = Flask(__name__)
CORS(app)

GRADIO_API_URL = "https://javahui-index-tts2-test.ms.show/"

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "running",
        "service": "TTS Proxy API"
    })

@app.route('/api/tts/generate', methods=['POST'])
def generate_tts():
    try:
        data = request.get_json()
        audio_url = data.get('audio_url')
        text = data.get('text')
        
        if not audio_url or not text:
            return jsonify({"error": "Missing parameters"}), 400
        
        client = Client(GRADIO_API_URL)
        result = client.predict(
            prompts=[handle_file(audio_url)],
            text=text,
            api_name="/gen_single_15"
        )
        
        return jsonify({
            "success": True,
            "audio_path": result
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
