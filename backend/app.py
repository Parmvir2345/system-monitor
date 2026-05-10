from flask import Flask, jsonify
from flask_cors import CORS
from metrics import get_metrics

app = Flask(__name__)
CORS(app)

@app.route('/api/metrics')
def metrics():
    data = get_metrics()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
EOF
