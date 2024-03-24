# YouTube Video Fetcher API

This repository contains a Flask application that continuously fetches the latest videos from YouTube based on a predefined search query and stores the video data in an external json file. It also provides a GET API endpoint to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query.

## Requirements

- Python 3.x
- Flask
- Requests library

## Installation

1. Clone the repository:

```

git clone https://github.com/Abhinav-Upadhyay03/FamPay-1.git

```

2. Install the required dependencies:

```

pip install -r requirements.txt

```

3. Obtain a YouTube Data API key from the Google Developer Console and replace the placeholder in the `callTheAPI` function with your actual API key.

## Usage

1. Run the Flask application:

```

python app.py

```

2. The server will continuously fetch the latest videos from YouTube in the background with a 10-second interval.

3. The server will provide the stored video data through its API endpoint. Upon running the code, a new `output.json` file will be created containing the required output.

## Database Schema

The database stores the following fields for each video:

- Video title
- Description
- Publishing datetime
- Thumbnail URLs

## Scalability and Optimization

To ensure scalability and optimization:
- The application uses asynchronous background tasks to continuously fetch data from the YouTube API without blocking the main thread.
- The application can be containerized using Docker for easier deployment and scaling.
