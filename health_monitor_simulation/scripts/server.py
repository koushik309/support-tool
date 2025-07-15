from flask import Flask, jsonify
from flask import Flask, jsonify
import time

app = Flask(__name__)
SERVER_START_TIME = time.time()

@app.route('/health')
def health():
    return jsonify({
        "status": "running",
        "uptime": round(time.time() - SERVER_START_TIME, 1),
        "version": "1.3.0"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=60000)