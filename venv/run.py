from flask import Flask, render_template, request, redirect, url_for
from link import insert_user, get_all_users

app = Flask(__name__)

@app.route('/')
def signup():
    users = get_all_users()
    return render_template('signup.html', users=users)

@app.route('/register', methods=['POST'])
def register():
    user_id = request.form['user_id']
    user_name = request.form['user_name']
    password = request.form['password']

    insert_user(user_id, user_name, password)

    return redirect(url_for('signup'))

if __name__ == '__main__':
    app.run(debug=True)
