from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # Git Pull 실행
        try:
            os.chdir('/home/ubuntu/flask_app')  # 프로젝트 디렉토리로 이동
            subprocess.run(['git', 'pull'], check=True)  # Git pull 실행
            subprocess.run(['sudo', 'systemctl', 'restart', 'flask_app'], check=True)  # 애플리케이션 재시작
            return jsonify({'status': 'success'}), 200
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500
    else:
        return jsonify({'status': 'method not allowed'}), 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
