


from ask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
      username = request.form['username']
      return redirect(url_for('name', username=username))
    return render_template('index.html', title='home')
@app.route('/<username>', methods=['GET', 'POST'])
def name(username):
  return render_template('index.html', title='name', username=username)
