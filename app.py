from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import CCcamTester
import os

app = Flask(__name__)
CORS(app) 

# هذه الدالة ستفتح صفحة الـ HTML الخاصة بك مباشرة
@app.route('/')
def home():
    return send_file('index.html')

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
    # تشغيل الخادم على المنفذ 5000
    app.run(debug=True, port=5000, host='0.0.0.0')
