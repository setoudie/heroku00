from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/test')
def test():
    return "render_template('login.html')"

@app.route('/test0')
def test0():
    return "render_template('login.html')"

if __name__ == '__main__':
    app.run()
