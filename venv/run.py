
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
      username = request.form.get('username')
      password = request.form.get('password')
   return render_template('index.html')

def signup():
   return render_template('signup.html')

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)