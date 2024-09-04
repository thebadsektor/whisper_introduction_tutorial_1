# TODO#1 - Import Libraries and Check availabity of GPU

def transcribe(file_path, model=None, language=None, verbose=False):    
    try:
        # TODO#2 - Import Libraries and Check availabity of GPU

        

        # TODO#3 - Establish Access to Audio File

        
        
        # TODO#4 - Perform transcription and store to `result`
        
        

        # TODO#5 - Create folder where the transcription will be saved to

        

        # TODO#6 - Loop through the result segments.
        pass #Delete this after TODO#2

        

    except RuntimeError:
        print("Not a valid file, skipping.")

#Call the transcribe() function:
file_path = 'sample_audio/audio.wav'
transcribe(file_path, model="base", language="en", verbose=True)