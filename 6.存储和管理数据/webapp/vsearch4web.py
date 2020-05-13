from flask import Flask, render_template, request, escape
from vsearch import search4letters

app = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log','a') as log:
        #print(str(dir(req)), res, file=log)  # 在 req 调用 dir，生成一个列表，然后将这个列表传递到 str，转换成一个字符串
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|') # 使用 sep 参数为每个打印出来的值指定一个分割值

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request,results)
    return render_template('results.html',
    the_phrase=phrase,
    the_letters=letters,
    the_title=title,
    the_results=results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
    the_title='Welcome to search4letters on the web!')

@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        #contents = log.read() # 一次性读取整个文件，并赋值给 contents 变量
        #contents = log.readlines() # 将所有日志数据行读入一个名为 contents 的列表
        for line in log:
            contents.append([]) # 向 contents 追加一个新的空列表
            for item in line.split('|'): # 根据竖线分解这一行，然后处理得到的 '分解列表' 中的各项
                contents[-1].append(escape(item)) # 在 contents 末尾的列表最后追加转义后的数据
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    #return escape(''.join(contents)) # 利用 escape 转义，解决不显示请求数据的问题
    return render_template('viewlog.html',
    the_title='View Log',
    the_row_titles=titles,
    the_data=contents,)

if __name__ == '__main__':
    app.run(debug=True)
