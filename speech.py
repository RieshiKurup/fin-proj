from openai import OpenAI

client = OpenAI()
audio_file = open(r"C:\Users\riesh\OneDrive\Documents\Sound Recordings\Recording (2).m4a")

translation = client.audio.translations.create(
    model="whisper-1", 
    file=audio_file,
)

print(translation.text)