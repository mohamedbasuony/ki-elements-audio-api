# ki-elements-audio-api
This repository is for the Ki-Elements Audio API, a Flask-based RESTful API designed to manage and serve audio files securely.

Prerequisites
- Install python on your machine.

Getting Started
- Clone the repository:
  git clone https://github.com/your-username/ki-elements-audio-api.git

- Go into its directory:
  cd ki-elements-audio-api

- Install the required dependencies:
  pip install -r requirements.txt

How To Use It:
- Run the flask application:
  python flask_audio_api.py

- Now accessible at http://localhost:5000

  Endpoints

  - Authentication is required before using any endpoint. Therefore, make sure to include the following username and password
    in your URL:
    Username: Basuony
    Password: 12345
    The URL should look something like this: http://Basuony:12345@127.0.0.1:5000/

  - Home Page
    URL: '/'
    Method: 'GET'
    Description: Retrieve a greeting message.

  - Get Audio Files
    URL: '/audio'
    Method: 'GET'
    Description: Get a list of all available audio files and their details

  - Get a Specific Audio File
    URL: '/audio/<file_name>'
    Method: 'GET'
    Description: Get a specific audio file using its name

  - Upload Audio File
    URL: 'audio'
    Method:'POST'
    Description: Upload a new audio file.
      JSON Schema used: http://json-schema.org/draft-07/schema#
      Request Body:
        {
          "file": {
            "filename": "your_filename.mp3",
            "data": "base64_encoded_audio_data_here"
                  }
        }


Testing: 
  To run the unittests available with the API: run the following line:
  python test_audio_api.py
  
  


