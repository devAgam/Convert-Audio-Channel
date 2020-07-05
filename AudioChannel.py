#Importing Needed Library
from pydub import AudioSegment
#Importing the Original Audio
sound = AudioSegment.from_wav('Original_Recording.wav')
# Declaring the number of chaneels Needed
sound = sound.set_channels(1)
# Declaring the number of chaneels Needed
sound.export("recfinal.wav", format="wav")
# Exporting Modified Audio As Needed                      
