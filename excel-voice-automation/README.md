# About
Voice dictaiting instead of keyboard writing in excel sheet.

## how to use

Download file and install packages, run app.py file and 
- run app.py script
- move your mouse to desirable cell
- start dictating (average speed)
- when you stop talking program will stop and fill all cells from up to down

Speech2Text class takes 3 arguments:
- recognizer (by default=sr.Recognizer()) 
- source (by default it's your built-in microphone, you can change it to external one)
- ambient_adjust (by default it's false, it's recommended if you are in loud enviroment)



## warning
currently PyAudio=0.2.11 does not work with new Python > 3.9
