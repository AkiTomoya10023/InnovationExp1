from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def load_notes():
    notes = []
    with open('notes.txt', 'r') as f:
        for line in f:
            notes.append(line.strip())
    return notes


def save_notes(notes):
    with open('notes.txt', 'w') as f:
        for note in notes:
            f.write(note + '\n')


@app.route('/')
def index():
    notes = load_notes()
    return render_template('index.html.jinja2', notes=notes)


@app.route('/add', methods=['POST'])
def add():
    note = request.form['note']
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    return redirect(url_for('index'))


@app.route('/delete', methods=['POST'])
def delete():
    id = request.form['id']

    try:
        id_int = int(id)

        if id_int > 0:
            notes = load_notes()

            if id_int <= len(notes):
                notes.pop(id_int - 1)
                save_notes(notes)
                return redirect(url_for('index'))

    except (ValueError, TypeError):
        pass

    # 显示给用户的错误消息
    error_msg = '无法删除所选笔记，请输入有效的笔记编号。'
    return render_template('index.html.jinja2', error_message=error_msg)


if __name__ == '__main__':
    app.run(debug=True)
