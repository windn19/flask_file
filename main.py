import pathlib

from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename


app = Flask(__name__)
BASEPATH = pathlib.Path('images')


@app.get('/')
def hello():
    return 'Hello world!!!'


@app.post('/load_file')
def upload_files():
    if 'files' in request.files:
        f = request.files['files']
        BASEPATH.mkdir(exist_ok=True)
        filename = secure_filename(f.filename)
        f.save(BASEPATH / filename)
    return jsonify({'status': 'Прочитано'})


@app.get('/get_file/<filename>')
def get_files(filename):
    return send_from_directory('images', filename)


if __name__ == '__main__':
    app.run(debug=True)

