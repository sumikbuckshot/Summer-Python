<<<<<<< HEAD
#!/usr/bin/python
import webbrowser
import time 
=======
import speech_recognition as sr
import time
import webbrowser
>>>>>>> 875133cb2ed1ac57a6246551006b41d6a2b69d52
from googlesearch import search
f=open('url.txt','w')
print("press 1 for keyboard and Press 2 for voice search")
choice=input()
if choice== '1':
<<<<<<< HEAD
	web=input("Please enter here : ")
	print(web)
	webbrowser.open_new_tab("https://www.google.com/search?q="+web)
	url=[]
	for i in search(web,stop=10):
		print(i)
		time.sleep(3)
		f.write(i+'\n')
		url.append(i)
	print(url)
	f.close()
else :

	
=======
        web=input("Please enter here : ")
        print(web)
        webbrowser.open_new_tab("https://www.google.com/search?q="+web)
        url=[]
        for i in search(web,stop=10):
                print(i)
                time.sleep(3)
                f.write(i+'\n')
                url.append(i)
        print(url)
        f.close()
elif choice=='2':
    def recognize_speech_from_mic(recognizer,microphone):
        with microphone as source:
                      audio=recognizer.listen(source)
        response={
                       "success": True,
                       "error": None,
                       "transcription": None,
            }
        try:
            reponse["transcription"]=recognizer.recognize_google(audio)
        except sr.RequestError:                        
            response["success"]= False
            response["error"]="Api unavailable"
        except sr.UnknownValueError :
            response["error"]+"Unable to recognize speech"
        return response
                
    recognizer = sr.Recognizer()
    microphone=sr.Microphone()
    print("Speak now")
    guess=recognize_speech_from_mic(recognizer,microphone)
    if response["success"]:
        webbrowser.open_new_tab("https://www.google.com/search?q="+guess)
        url1=[]
        for j in search(guess,stop=10):
            print(j)
            time.sleep(3)
            f.write(j+'\n')
            url1.append(j)
        print(url1)
        f.close()
    else :
         print("i didn't get you, sorry")
else :
      print("wrong input")
>>>>>>> 875133cb2ed1ac57a6246551006b41d6a2b69d52
