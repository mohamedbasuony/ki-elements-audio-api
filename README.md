# Ki-Elements Audio API

This repository is for the Ki-Elements Audio API, a Flask-based RESTful API designed to manage and serve audio files securely.

## Prerequisites

Make sure you have Python installed on your machine.

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/ki-elements-audio-api.git
    ```

2. Go into its directory:

    ```bash
    cd ki-elements-audio-api
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## How To Use It

1. Run the Flask application:

    ```bash
    python flask_audio_api.py
    ```

2. Now accessible at [http://localhost:5000](http://localhost:5000).

## Endpoints

- **Authentication is required before using any endpoint. Include the following username and password in your URL:**
  - **Username:** Basuony
  - **Password:** 12345
  - **URL example:** [http://Basuony:12345@127.0.0.1:5000/](http://Basuony:12345@127.0.0.1:5000/)

1. **Home Page**
   - **URL:** `/`
   - **Method:** `GET`
   - **Description:** Retrieve a greeting message.

2. **Get Audio Files**
   - **URL:** `/audio`
   - **Method:** `GET`
   - **Description:** Get a list of all available audio files and their details.

3. **Get a Specific Audio File**
   - **URL:** `/audio/<file_name>`
   - **Method:** `GET`
   - **Description:** Get a specific audio file using its name.

4. **Upload Audio File**
   - **URL:** `/audio`
   - **Method:** `POST`
   - **Description:** Upload a new audio file.
   - **JSON Schema:** [http://json-schema.org/draft-07/schema#](http://json-schema.org/draft-07/schema#)
   - **Request Body Example:**
     ```json
     {
       "file": {
         "filename": "your_filename.mp3",
         "data": "base64_encoded_audio_data_here"
       }
     }
     ```

## Testing

To run the unit tests available with the API, use the following command:

```bash
python test_audio_api.py
```
