from flask import Flask, render_template, send_file, redirect, url_for, request
from music_generator import create_melody
import os

app = Flask(__name__)

# Store the path of the latest generated melody
latest_melody_path = "Songs/random_melody.mid"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_melody():
    # Get the filename from the form input
    filename = request.form['filename']
    length = int(request.form['length'])
    tempo = int(request.form['tempo'])
    scale = int(request.form['scale'])

    # Ensure the filename ends with .mid
    if not filename.endswith('.mid'):
        filename += '.mid'

    # Generate the melody and save it with the custom filename
    global latest_melody_path
    latest_melody_path = os.path.join('static\Songs', filename)
    create_melody(filename=latest_melody_path, tempo=tempo, length=length, scale=scale)

    return redirect(url_for('download_melody'))

@app.route('/download')
def download_melody():
    return send_file(latest_melody_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)