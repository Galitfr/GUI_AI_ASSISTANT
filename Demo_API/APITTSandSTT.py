from importlib import import_module
from pathlib import Path
from openai import OpenAI
from audioplayer import AudioPlayer

client = OpenAI()

def TTS_Demo(inputText):
    if len(inputText)<1: return 
    speech_file_path = Path(__file__).parent / "speech1.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=inputText
    )
    
    # Assuming the response's content is the binary data of the speech file
    with open(speech_file_path, 'wb') as file:
        file.write(response.content)
    # Play the text-to-speech audio
    AudioPlayer(str(speech_file_path)).play(block=True)


#TTS_Demo("I like basketball")

# Transcript using whisper-1 model
def STT_Demo():
    audio_file= open("speech.mp3", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        #response_format="text"
    )
    print(transcription.text)   # the response is in JSON format 

STT_Demo()

# Translation of audio to English text, using whisper-1 model
def STT_Translation():      
    audio_file= open("speech.mp3", "rb") # In any of the supported formats/languages
    translation = client.audio.translations.create(
      model="whisper-1", 
      file=audio_file
    )
    print(translation.text)    

#STT_Translation()
    
# transcript and play the audio, in a streaming fashion. Somewhat slow.
def TTS_Streaming():
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Say this is a test"}],
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
            # Text to speech and play the audio
            TTS_Demo(chunk.choices[0].delta.content)

#TTS_Streaming()