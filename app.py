"""
Project Name: YouTube Transcript Summarizer
YouTube Transcript Summarizer API
"""

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/', methods=['GET'])
def respond():

    # Retrieve the video_id from url parameter
    vid_id = request.args.get("video_id", None)

    if "youtube.com" in vid_id:
        
        try:
            v_id = vid_id.split("=")[1]
            
            try:
                v_id = v_id.split("&")[0]
            
            except:
                v_id = "False"
        
        except:
            v_id = "False"
    
    elif "youtu.be" in vid_id:
        
        try:
            v_id = vid_id.split("/")[3]
        
        except:
            
            v_id = "False"
    
    else:
        v_id = "False"


    # For debugging
    # print(f"got name {v_id}")

    body = {}
    data = {}

    # Check if user doesn't provided  at all
    if not v_id:
        data['message'] = "Failed"
        data["error"] = "no video id found, please provide valid video id."
    
    # Check if the user entered a invalid instead video_id
    elif str(v_id) == "False":
        data['message'] = "Failed"
        data["error"] = "video id invalid, please provide valid video id."
    
    # Now the user has given a valid video id
    else:
        data['message'] = "Success"
        data['id'] = v_id
        data['count'] = 0
    
    body["data"] = data

    # Return the response in json format
    return buildResponse(200, body)


# Welcome message to our server
@app.route('/')
def index():

    body = {}
    body['message'] = "Success"
    body['data'] = "Welcome to YTS API."

    return buildResponse(200, body)


def buildResponse(statusCode, body):

    res = {
            "statusCode": statusCode,
		    "headers": {
			"Content-Type": "application/json",
		    },
		    "body": body,
        }
    return jsonify(res)


if __name__ == '__main__':

    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True)

# Deployment to Heroku Cloud.