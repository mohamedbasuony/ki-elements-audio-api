import json
import unittest
import flask
from base64 import b64encode
from flask_audio_api import app, audio_files_db, users


def get_auth_headers(username, password):
    return {
        'Authorization': 'Basic ' + b64encode(f'{username}:{password}'.encode()).decode('utf-8')
    }


class TestApi(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    # helper function for the tests of  post_audio

    def post_audio_request(self, data):
        return self.app.post('/audio', json=data)

    # login conditions: successful or not
    # Redundant but left just in case in the future the login changes to be only on this step and not
    # on each endpoint also

    def test_login_successful(self):
        response = self.app.get('/', headers=get_auth_headers('Basuony', '12345'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, Basuony!', response.data)

    def test_login_failed(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 401)

    # GET request conditions: all or one

    def test_get_all_audio_files(self):
        response = self.app.get('/audio', headers=get_auth_headers('Basuony', '12345'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your application logic

    def test_get_one_audio_file(self):
        response = self.app.get('/audio/patient1.mp3', headers=get_auth_headers('Basuony', '12345'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your application logic

    # POST request condition: success or not

    def test_post_audio_success(self):
        # Mocking a valid POST request data
        mock_request_data = {
            "file": {
                "filename": "patient3.mp3",
                "data": "SGVsbG8gd29ybGQhCkhlbGxvLCBXb3JsZCEK"
            }
        }

        response = self.app.post('/audio', headers=get_auth_headers('Basuony', '12345'),json=mock_request_data)
        # Asserting that the response contains the expected message and status code
        self.assertEqual(response.status_code, 200)
        self.assertIn('Audio file uploaded successfully', response.get_json()['message'])

        # Asserting that the audio file entry is added to the database
        self.assertIn('patient3.mp3', response.get_json()['file_path'])

    def test_post_audio_missing_file(self):
        # Mocking a request with missing 'file' property
        mock_request_data = {}

        response = self.app.post('/audio', headers=get_auth_headers('Basuony', '12345'),json=mock_request_data)

        # Asserting that the response contains the expected error message and status code
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing file in the request', response.get_json()['error'])

    def test_post_audio_invalid_file_data(self):
        # Mocking a request with invalid file data
        mock_request_data = {
            "file": {
                "filename": "patient3.mp3"
                # Missing 'data' property
            }
        }

        response = self.app.post('/audio', headers=get_auth_headers('Basuony', '12345'),json=mock_request_data)

        # Asserting that the response contains the expected error message and status code
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid file data in the request', response.get_json()['error'])


if __name__ == '__main__':
    unittest.main()
