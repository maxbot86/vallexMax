from utils.prompt_making import make_prompt
from utils.generation import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav

def cloneVoice(modelVoice, msg, outputFile):
    audio_array = generate_audio(msg, prompt=modelVoice)
    write_wav(outputFile, SAMPLE_RATE, audio_array)

def trainVoiceModel(modelName, pathAudioExample, transcrption=''):
    if transcrption =='':
        make_prompt(name=modelName, audio_prompt_path=pathAudioExample)
    else:
        make_prompt(name=modelName, audio_prompt_path=pathAudioExample,transcript=transcrption)

# Descargar y cargar todos los modelos
#preload_models()

#===============================================