from flask import Flask, render_template, request, jsonify
import requests
import json
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()
API_URL = os.getenv("HUGGING_FACE_API_URL")
headers = {'Authorization': f'Bearer {os.getenv("HUGGING_FACE_API_KEY")}'}

# 启动网站
app = Flask(__name__)


#  AI从列表里获取传入的图像信息
def query(file):

    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": file.content_type  # 👈 自动获取
    }

    response = requests.post(
        API_URL,
        headers=headers,
        data=file.read()
    )

    print("status:", response.status_code)
    print("response:", response.text)

    if response.status_code != 200:
        print("Request failed:", response.status_code)
        return None

    try:
        return response.json()
    except Exception as e:
        print("JSON解析失败:", e)
        return None


@app.route('/')
def index():
    return render_template('./index.html')

# 图片的发送位置
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file1']
    modeldata = query(file)
    return jsonify(modeldata)


app.run(host='0.0.0.0', port=81)