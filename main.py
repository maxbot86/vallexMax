from cloneVoice import *

# Descargar y cargar todos los modelos
preload_models()

#===============================================
msg = """
Hello, how are you? My voice was make by an artificial intelligence. Good bye  and see you late!
"""
cloneVoice("dany", msg, "dany_cloned_03.wav")


msg = """
Hi, i am really afraid. Could you readme an Story?.
"""
cloneVoice("dany", msg, "dany_cloned_04.wav")