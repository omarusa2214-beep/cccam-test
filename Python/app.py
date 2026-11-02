from flask import Flask, request, jsonify
from flask_cors import CORS
import CCcamTester

app = Flask(__name__)
CORS(app) 

@app.route('/api/check', methods=['POST'])
def check_cline():
    data = request.json
    cline = f"C: {data['host']} {data['port']} {data['user']} {data['pass']}"
    
    is_working = CCcamTester.TestCline(cline)
    
    return jsonify({
        "status": "success",
        "connected": is_working
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
