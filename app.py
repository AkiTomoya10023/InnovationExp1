from flask import Flask, render_template, request

app = Flask(__name__)

# 定义本地记事本文件路径
NOTES_FILE = 'notes.txt'


# 定义函数，用于读取本地记事本文件
def read_notes():
    with open(NOTES_FILE, 'r') as f:
        notes = f.read().splitlines()
    return notes


# 定义函数，用于添加记录到本地记事本文件
def add_note(note):
    with open(NOTES_FILE, 'a') as f:
        f.write(note + '\n')


# 定义路由，用于显示所有记录和添加新记录
@app.route('/', methods=['GET', 'POST'])
def notes():
    if request.method == 'POST':
        note = request.form['note']
        add_note(note)
    notes = read_notes()
    return render_template('index.html.jinja2', notes=notes)


if __name__ == '__main__':
    app.run(debug=True)
