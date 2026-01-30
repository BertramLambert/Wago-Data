from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>這是 cc100 容器跑出來的網頁！</h1><p>Python 版本：3.14.2</p>"

if __name__ == "__main__":
    # 必須監聽 0.0.0.0 才能從容器外存取

    app.run(host='0.0.0.0', port=5000)
