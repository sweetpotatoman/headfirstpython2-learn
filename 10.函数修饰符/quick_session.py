from flask import Flask, session # 导入 session 函数，让 Web 应用能够记住状态

app = Flask(__name__)

app.secret_key = 'YouWillNeverGuess' # 秘密密钥，为 flask 的 cookie 生成技术提供一个秘密密钥作为种子，flask 利用这个密钥加密你的 cookie，然后才可以把它传输到 浏览器


@app.route('/setuser/<user>') # 这个 URL 希望你提供一个值来赋给 "user" 变量
def setuser(user: str) -> str:
    session['user'] = user  # user 变量的值赋给 session 字典中的 "user" 键
    return 'User value set to: ' + session['user']


@app.route('/getuser')
def getuser() -> str:
    return 'User value is currently set to: ' + session['user'] # 访问 session 中的数据


if __name__ == '__main__':
    app.run(debug=True)
