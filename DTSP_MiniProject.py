from gtts import gTTS 
import os 
import speech_recognition as sr

def text_to_speech():
    print('************************************')
    print('Welcome to Text to Speech Convertor')
    print('************************************')
    fh = open("text1.txt", "r")
    myText = fh.read().replace("\n", " ")

    # Language we want to use 
    language = 'en'

    output = gTTS(text=myText, lang=language, slow=False)

    output.save("output.mp3")
    fh.close()

    # Play the converted file 
    os.system("start output.mp3")
    print('The program ends here, the audio is ready to play!')
    print("Thank you for using text to speech convertor!")
    print('*************************************************************')

def speech_to_text():
    print('************************************')
    print('Welcome to Speech to Text Convertor')
    print('************************************')
    sound = 'test_Recording.wav'
    recorder = sr.Recognizer()
    with sr.AudioFile(sound) as source:
        recorder.adjust_for_ambient_noise(source)
        print('Converting Audio File to text....')
        audio = recorder.listen(source)

        try:
            print('Converted Audio Is : \n ' + recorder.recognize_google(audio))
        except Exception as e:
            print(e)

        print("------------------------------------------------2")
        print('The program ends here, the text is ready!')
        print("Thank you for using speech to text convertor!")
        print('*********************************************************')

print("-----------------------------------------------------------------")
print("Hello Everyone!!")
print("1.Text to Speech Convertor")
print('2.Speech to Text Convertor')
choice = int(input('Enter Your Choice: '))
if choice == 1:
    text_to_speech()
elif choice == 2:
    speech_to_text()
else:
    print('INVALID CHOICE')