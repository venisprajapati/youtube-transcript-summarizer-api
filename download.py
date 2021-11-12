def makeTextFile(name, content):
    file = open(f"../youtube-transcript-summarizer-frontend/src/transcripts/{name}.txt","w")
    
    file.write(f"{name} Transcript:\n")
    file.write(content)
    file.close()
