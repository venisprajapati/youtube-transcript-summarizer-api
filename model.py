from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")

def summarizer_model(video_id):
  YouTubeTranscriptApi.get_transcript(video_id)
  transcript = YouTubeTranscriptApi.get_transcript(video_id)
  transcript

  result=""
  for i in transcript:
    result += ' '+ i['text']
  print(len(result))

  summarizer = pipeline('summarization')

  num_iters = int(len(result)/1000)
  summarized_text = [] 
  total_len = 0
  for i in range(0,num_iters+1):
    start = 0
    start = i*1000
    end = (i+1)*1000
    out = summarizer(result[start:end])
    out = out[0]
    out = out['summary_text']
    summarized_text.append(out)
    total_len += len(out)

    script = ""
    for i in summarized_text:
      script += i.strip()

  return script
  # print(summarized_text)
  # print(total_len)

