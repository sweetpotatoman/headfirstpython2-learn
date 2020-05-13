from flask import Flask, session

from checker import check_logged_in

app = Flask(__name__)

app.secret_key = 'YouWillNeverGuess'

@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp.'

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True # 将 session 字典中的 "logged_in" 键设置为 True
    return 'You are now logged in.'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in') # 使用 pop 方法从 session 字典删除 logged_in 键
    return 'You are now logged out.'

# @app.route('/status')
# def check_status() -> str:
#     if 'logged_in' in session: # 检查 session 字典还存在 logged_in 键没
#         return 'You are currently logged in.'
#     return 'You are NOT logged in.'


@app.route('/page1')
@check_logged_in
def page1():
    return 'This is page 1.'


@app.route('/page2')
@check_logged_in
def page2():
    return 'This is page 2.'


@app.route('/page3')
@check_logged_in
def page3():
    return 'This is page 3.'


if __name__ == '__main__':
    app.run(debug=True)
