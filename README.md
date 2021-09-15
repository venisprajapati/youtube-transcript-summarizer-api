# youtube-transcript-summarizer-api

Youtube Transcript Summarizer API

# Project Overview
This project is an integration of web development and the very emerging technology, Machine Learning. This Project aims to provide summarized documentation of a video that are too long to be watched. Today education is more dependent on online sources rather than the offline source, and no one has much time to spent on lecture videos that are too long to watch. So, to resolve this, there should be a tool which can provide a summarization of the video and therefor save time.

# Problem and Solution Statement
Enormous number of video recordings are being created and shared on the YouTube throughout the day. It becomes really difficult to spend time in watching such videos which may have a longer duration than expected and sometimes our efforts may become futile if we aren’t able to find relevant information out of it. Summarizing transcripts of such videos will allows us to quickly look out for the important patterns in the video and helps us to save time and efforts to go through the whole content of the video.

# Benchmark (How this solution is better?)
There are many available applications to do so. But this project aims to build a chrome extension, so that the user can use it efficiently. Other applications which aim to solve this particular problem, need the link of a particular video to be provided by the user while using this extension, you can get the summarized text of your video within a couple of clicks.

# Implementation strategy
So basically, it will be a chrome extension, having an option to copy to current URL of the video being selected. After providing the link, it will access the transcript of the particular audio using the YouTube transcript API and then the transcript will be provided to a machine learning model will in return provide the summarized text of the transcript. The summarized text would be downloadable by the user.

Tech:
- Python
- Flask

Deployment:
- Heroku

## This Repository contains all the files related to the API used in the project.
## Files related to the chreome extension and the model could be found at : https://github.com/19IT114/Youtube-Transcript-Summarizer
