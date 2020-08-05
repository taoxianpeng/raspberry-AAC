from flask import Flask
from flask import render_template
from flask import request as flask_request

app = Flask(__name__)

@app.route('/')
def index():
    # render_template('index.html')
    return render_template('index.html')
@app.route('/setting')
def settting():
    pass

if __name__ == "__main__":
    app.run(threaded=True)