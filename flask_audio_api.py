from flask import Flask, request, jsonify, send_file
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application & Flask-HTTPAuth extension
app = Flask(__name__)
auth = HTTPBasicAuth()

# Sample user data for authentication
users = {
    "Basuony": generate_password_hash("12345")
}

# Database of audio files with their IDs and paths
audio_files_db = {
    'patient1.mp3': {'id': 1, 'path': 'patient1.mp3'},
    'patient2.mp3': {'id': 2, 'path': 'patient2.mp3'}
}


# Authentication verification function
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username


# Home route, accessible only to authenticated users
@app.route('/')
@auth.login_required
def index():
    return "Hello, {}!".format(auth.current_user())


# Endpoint to get a list of available audio files
@app.route('/audio', methods=['GET'])
@auth.login_required
def get_audio_files():
    # JSON response with audio files details
    audio = [{"audio_id": value["id"], "audio_name": key} for key, value in audio_files_db.items()]
    return jsonify(audio), 200


# Endpoint to get a specific audio file by name
@app.route('/audio/<file_name>', methods=['GET'])
@auth.login_required
def get_audio(file_name):
    # Check if the requested audio file exists before returning it
    audio = audio_files_db.get(file_name)
    if audio:
        return send_file(audio["path"], as_attachment=True), 200
    else:
        return jsonify({'404 Error!': 'The Audio file was not found'}), 404


# Endpoint to upload a new audio file
@app.route('/audio', methods=['POST'])
@auth.login_required
def post_audio():
    try:
        # Retrieve JSON data from the POST request
        request_data = request.get_json()

        # Check if the required 'file' property is present in the request data
        if 'file' not in request_data:
            return jsonify({'error': 'Missing file in the request'}), 400

        file_data = request_data['file']

        # Check if the 'filename' and 'data' properties are present in the 'file' property
        if 'filename' not in file_data or 'data' not in file_data:
            return jsonify({'error': 'Invalid file data in the request'}), 400

        # Extract filename and data from the request
        filename = file_data['filename']
        data = file_data['data']

        # Update the audio_files_db with the new audio file information
        audio_files_db[filename] = {
            'id': len(audio_files_db) + 1,
            'path': f'/{filename}'
        }

        return jsonify(
            {'message': 'Audio file uploaded successfully', 'file_path': audio_files_db[filename]['path']}), 200
        # Will never be triggered, added just in case this code was scaled on a real server
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
