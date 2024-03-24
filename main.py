from flask import Flask, jsonify
import requests
import threading
import json


app = Flask(__name__)


@app.route('/')
def callTheAPI():
    # Define the URL for the YouTube Data API
    youtube_api_url = 'https://www.googleapis.com/youtube/v3/search'
    
    # Define the parameters for the request (including your API key and keyword)
    params = {
        'key': 'AIzaSyAxiwtZAYm5yvIN6_ihU2WbzDqoGAYmntM',  
        'q': 'cricket',
        'part': 'snippet',
        'order': 'date',
        'maxResults': '50',
    }

    # Video title, description, publishing datetime, thumbnails URLs
    videoTitle = []
    description = []
    time = []
    thumbNail = []
    # Make the GET request to the YouTube Data API
    response = requests.get(youtube_api_url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        for ele in data['items']:
            videoTitle.append(ele['snippet']['title'])
            description.append(ele['snippet']['description'])
            time.append(ele['snippet']['publishedAt'])
            thumbNail.append(ele['snippet']['thumbnails']['default'])

        jsonFile = []
        for i in range(0, len(videoTitle)):
            jsonFile.append({
                "Title": videoTitle[i],
                "Description": description[i],
                "Published_Time": time[i],
                "ThumbnailURL": thumbNail[i]
            })

        #Store the file to a json file
        file_path = "output.json"
        with open(file_path, 'w') as json_file:
            json.dump(jsonFile, json_file, indent=4)
        
        # Return the JSON response from the YouTube Data API
        return jsonify(jsonFile)
    else:
        # Return an error message if the request was unsuccessful
        return jsonify({'error': 'Failed to fetch data from YouTube API'}), response.status_code


def get_youtube_data():
    
    #This part will update the database every 10
    timer = threading.Timer(10, callTheAPI)
    timer.start()
    


if __name__ == '__main__':
    app.run(debug=True)
