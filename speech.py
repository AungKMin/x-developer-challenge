from gtts import gTTS
import os
import json

def create_text_from_answer(answer):
    answer_str = "{" + ''.join(answer)
    answer_json = json.loads(answer_str)
    intro = "Good morning! Here are your stock news from X!"
    body = ""
    print(answer_json)
    for stock in answer_json['stocks']:
        text = "For " + stock['name'] + ", X is feeling " + stock['sentiment'] + " for these following reasons. " + stock['reason'] + " "
        body += text
    end = "That's all for today, have a great one!"
    return intro + body + end

def create_mp3(string, file_name):
    myobj = gTTS(text=string, lang='en', slow=False)
    myobj.save(file_name)

def play_mp3(file_name):
    os.system(file_name)    
