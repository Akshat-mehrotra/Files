from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect
from servo import Servo

app = Flask(__name__)

main = Servo(pin=5)

@app.route('/')
def index():
    name = 'mainDoor'
    return render_template('index.html', name=name)

@app.route("/main", methods=['POST'])
def main():
    main.run()
    return redirect('/')
    return 'LMAO ME DUDE'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 80, debug=True)
