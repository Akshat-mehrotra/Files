from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect
from servo import Servo
from flask.ext.uploads import Uploadset, configure_uploads, ALL


app = Flask(__name__)

mainDoor = Servo(pin=5)

upfile = UploadSet('file', ALL)
app.config['UPLOADED_FILES_DEST'] = "/home/pi/uploaded_files"
configure_uploads(app, upfile)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        func = ['door',]
        return render_template('index.html', func=func)

    elif request.method == 'POST' and 'file' in request.files['file']:
        filename = upfile.save(request.file['file'])

        return '''<h1>DONE UPLOADING</h1>
                <form action='/'>
                    <input type='submit' value='GOBACK TO MAIN PAGE' style="height:120px; width:120px">
                </form>'''


@app.route("/maindoor", methods=['POST'])
def door():
    mainDoor.run()
    return redirect('/')
    


@app.route('/upload')
def upload():
    pass
if __name__ == '__main__':
    app.run(debug=True)
