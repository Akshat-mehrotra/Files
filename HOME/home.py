from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect
from servo import Servo
from flask.ext.uploads import Uploadset, configure_uploads, IMAGE
import os

app = Flask(__name__)

direct = ''

mainDoor = Servo(pin=5)

upfile = UploadSet('file', IMAGE)
app.config['UPLOADED_FILES_DEST'] = "/home/pi/uploaded_files/"
configure_uploads(app, upfile)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':

        func = ['door',]
        return render_template('index.html', func=func)


    elif request.method == 'POST' and 'file' in request.files:

        app.config['UPLOADED_FILES_DEST'] += request.files['file'].filename.split(".")[1]
        filename = upfile.save(request.files['file'])

        return '''<h1>DONE UPLOADING</h1>
                <form action='/'>
                    <input type='submit' value='GOBACK TO MAIN PAGE' style="height:120px; width:120px">
                </form>'''


@app.route("/maindoor", methods=['POST'])
def door():
    mainDoor.run()
    return redirect('/')
    

@app.route("/browse/<path>")
def browse(path=os.cwd()):
    
    direct += path
    if not os.path.isfile(direct):

        files = [f for f in os.listdir(direct)]
        return render_template('browse.html', files=files)

    return "<img src='{{direct}}' height='500', width='500'>"


if __name__ == '__main__':
    app.run(debug=True)
