from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    title = 'ABCD'
    return render_template('index.html',title=title)

@app.route('/data')
def data():
    return 'test'