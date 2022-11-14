import pyaudio
import wave
from google.cloud import speech
import os
import webbrowser

apiKey = "AIzaSyBErjAOCfpvjuI5IWUZYN2YFnRZaaqRNJQ"

sampleRate = 44100 
Format = pyaudio.paInt16
chunk = 1024
Channels = 2
buffer=1024 
recTime = 3
fileName = "recording.wav"

p = pyaudio.PyAudio()
stream = p.open(format=Format, channels=Channels,rate=sampleRate,input=True,frames_per_buffer=buffer)

#records the input
frames = []
print("Recording...")
for i in range(0, int(sampleRate / buffer * recTime)):
    data = stream.read(buffer)
    frames.append(data)
print("Done")
stream.start_stream()
stream.close
p.terminate()

#Generates the wav file
wf = wave.open(fileName, 'wb')
wf.setnchannels(Channels)
wf.setsampwidth(p.get_sample_size(Format))
wf.setframerate(sampleRate)
wf.writeframes(b''.join(frames))
wf.close()



#Speech detection time BB
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'
speechClient = speech.SpeechClient()

#reading thee file data
with open(fileName,"rb") as f1:
    data = f1.read()
Audio = speech.RecognitionAudio(content=data)

#Configuring the recognition
audio_config = speech.RecognitionConfig(
    sample_rate_hertz=sampleRate,
    language_code="en-US",
    audio_channel_count = 2
)

#generating speech transcription

transcription = speechClient.recognize(config=audio_config,audio=Audio).results[0].alternatives[0].transcript
print(transcription)

Url = "https://www.google.com/search?q="

for word in transcription.split(" "):
    Url = Url + word + "+" 
Url = Url + "&client=opera-gx&hs=bTi&tbm=isch&sxsrf=ALiCzsbzINz5Icxs6cnQH8jEwPTUnIzrgQ:1668451339588&source=lnms&sa=X&ved=2ahUKEwit567Lqa77AhURmVwKHZvwCaQQ_AUoAnoECAoQBA&biw=1879&bih=962&dpr=1"
browser = webbrowser.open(Url,0)

input()