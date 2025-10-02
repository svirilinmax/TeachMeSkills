"""
📋 Чего должен добиться студент:
	1.	Подключиться к PostgreSQL через psycopg2.
	2.	Создать таблицу wishes, если её нет.
	3.	Реализовать вставку новых пожеланий через POST.
	4.	Реализовать выборку всех пожеланий и передать их в шаблон.
	5.	(По желанию) Добавить новую страницу или кнопки — например, очистка списка.
"""
from flask import Flask, render_template, request, redirect, flash
import psycopg2

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Для работы flash-сообщений


def get_connection():
    return psycopg2.connect(
        dbname="wish_list",
        user="postgres",
        password="postgres",
        host="127.0.0.1",
        port="5432"
    )


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']

        if len(name.strip()) == 0 or len(message.strip()) == 0:
            flash('Имя и сообщение не могут быть пустыми!', 'error')
            return redirect('/')

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO wishes (name, message) VALUES (%s, %s)", (name, message))
        conn.commit()
        conn.close()
        flash('Пожелание успешно добавлено!', 'success')
        return redirect('/')

    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, name, message, created_at FROM wishes ORDER BY created_at DESC')
    wishes = cur.fetchall()
    conn.close()

    return render_template('wishes.html', wishes=wishes)


@app.route('/delete/<int:wish_id>', methods=['POST'])
def delete_wish(wish_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM wishes WHERE id = %s", (wish_id,))
    conn.commit()
    conn.close()
    flash('Пожелание удалено!', 'info')
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port=5001)