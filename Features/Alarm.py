import datetime
from playsound import playsound

#---- Jarvis Will Speak Through This Function :-

def Say(audio):
    import pyttsx3
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    engine.setProperty('rate',190)
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print("")

def Alarm():

    Say("When To Scheduled The Alarm ?")
    print("Enter Time is 24 Hour Format.")
    print("Enter Time Like This :17:24.")

    query11 = input("Enter Time :")
    
    while True:
        current_time = datetime.datetime.now() 
        now = current_time.strftime("%H:%M") 

        if now == query11: 
            Say("Time To Get Up!.")   
            playsound(str('My System\\DataBase\\Files\\alarm.mp3'))
            Say("Alarm Closed!")

        elif now>query11:
            break

Alarm()
