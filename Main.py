#---- Jarvis Will Listen Through This Function :-

def Listen():

    import speech_recognition as sr

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(": Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,0,3)

    try:
        print(": Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f": Your Command : {query}\n")
        print(" ")

    except:
        return ""

    return query.lower()

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

#---- Jarvis Will Start From This Function :-

def MainExecutor():

    print("")
    Say("Turning On The System")
    print("")
    print(">> Project Name : JARVIS ")
    print(">> Working : Assistant ")
    print(">> Level : Advance")
    print("")
    Say("Hello Sir. Wait While The System Is Starting....")
    
    import nltk
    nltk.download('punkt')
    #---- Jarvis Will Train Itself Using This Function

    from Brain.Training import TrainTalks , TrainTasks

    TrainTasks()
    TrainTalks()

    Say("Training Completed....")

    #---- Jarvis Will Start Taking Command From This Function

#---- Jarvis Will Be In a Loop Using This Function :-

def Start():

    Command = Listen()

    from Brain.Neurons import TalksExecutor , TasksExecutor

    Talks = TalksExecutor(Command)

    if str(Talks)=="None":
        pass

    else:
        Say(Talks)

    Tasks = TasksExecutor(Command)

    return Tasks, Command

#---- Executing :-

def BestVer():
        
    MainExecutor()

    while True:

        Task , Command = Start()

        from Features.Functions import FTasker

        FTasker(Task,Command)
