import datetime
from time import sleep
import keyboard
import requests
from bs4 import BeautifulSoup
import os
from pywikihow import search_wikihow
import pyautogui
import speech_recognition as sr
from googletrans import Translator
import datetime
from datetime import date
from PyDictionary import PyDictionary
import webbrowser
import geocoder
import wikipedia
import pywhatkit
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import wolframalpha
from PIL import Image
import speedtest
import pyjokes

#---- These are Some Functions That Will FullFill Your Requirment.

#---- Website opener Function - Done

def LaunchWebsite(name):
    url = str(name).replace("launch ","")
    url = str(url).replace("visit ","")
    Say(f"Opening The Website : {url}")
    import webbrowser

    if "facebook" in url:
        webbrowser.open("https://www.facebook.com")

    elif "instagram" in url:
        webbrowser.open("https://www.instagram.com")

    elif "youtube" in url:
        webbrowser.open("https://www.youtube.com")

    elif "drive" in url:
        webbrowser.open("https://drive.google.com/")

    elif "gmail" in url:
        webbrowser.open("https://mail.google.com/mail/")

    elif "twitter" in url:
        webbrowser.open("https://twitter.com/")

    else:
        url2 = "https://www." + str(url).replace(" ","") + ".com"
        webbrowser.open(url2)

#---- Open Apps Function - Done

def ApplicationOpener(name):
    typo = str(name).replace("open ","")
    typo = str(typo).replace("start ","")
    import pyautogui

    if "chrome" in typo:
        pyautogui.hotkey("win")
        sleep(1)
        pyautogui.write(typo)
        sleep(1)
        pyautogui.press('enter')
        import keyboard
        keyboard.press_and_release("alt + space")
        pyautogui.press("x")

    else:
        pyautogui.hotkey("win")
        sleep(1)
        pyautogui.write(typo)
        sleep(1)
        pyautogui.press('enter')   

#---- Make notes Function - Done

def NotesMaker():
    Say("Tell Me, What To Note ?")
    note = Listen()
    ApplicationOpener('notepad')
    sleep(1)
    import pyautogui
    pyautogui.write(note)
    import keyboard
    keyboard.press_and_release("ctrl + s")
    sleep(2)
    date = datetime.datetime.now().strftime("%H-%M-%M")
    keyboard.write(f"{date}.txt")
    keyboard.press('enter')
    sleep(1)
    keyboard.press_and_release("alt + f4")

#---- Typing Function - Done

def TypeFunction():
    Say("What You Want Me To Type Sir ?")
    typeeee = Listen()
    import keyboard
    keyboard.write(typeeee)
    
#---- System Specification Function - Done

def SystemInfo():
    import platform
    info = {}
    platform_details = platform.platform()
    info["platform details"] = platform_details
    system_name = platform.system()
    info["system name"] = system_name
    processor_name = platform.processor()
    info["processor name"] = processor_name
    architecture_details = platform.architecture()
    info["architectural detail"] = architecture_details
    for i, j in info.items():
        Say(i)
        Say(j)

#---- IP ADDress Teller Function - Done

def IpAdd():
    import socket
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    Say("Your Computer Name is:" + hostname)
    Say("Your Computer IP Address is:" + IPAddr)

#---- IP ADDress Changer Function - Done

def ChangeIp():
    import ipaddress
    ip = ipaddress.IPv4Address('192.168.1.52')
    print("Total no of bits in the ip:", ip.max_prefixlen)
    print("Is multicast:", ip.is_multicast)
    print("Is private:", ip.is_private)
    print("Is global:", ip.is_global)
    print("Is unspecified:", ip.is_unspecified)
    print("Is reversed:", ip.is_reserved)
    print("Is loopback:", ip.is_loopback)
    print("Is link-local:", ip.is_link_local)
    ip1 = ip + 1
    print("Next ip:", ip1)
    ip2 = ip - 1
    print("Previous ip:", ip2)
    print("Is ip1 is greater than ip2:", ip1 > ip2)
    Say("I Have Changed Your IP Address.")

#---- Keyboard Function - Done

def PressKey(query):
    query = str(query).replace("press ","")
    keyboard.press_and_release(query)

#---- Zoom In Function - Done

def ZoomIn():
    import keyboard
    keyboard.press_and_release("ctrl + plus")

#---- Zoom Out Function - Done

def ZoomOut():
    import keyboard
    keyboard.press_and_release("ctrl + -")

#---- Weather Function - Done

def Temperature(Name):
    se = f"temperature in {Name}"
    url = f"https://www.google.com/search?q={se}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div",class_="BNeawe").text
    Say(f"Temperature In {Name} Is {temp} .")

#---- Screen Shot Function - Done

def Screenshot():
    Say("What Should I Name That File ?")
    FileName = Listen()
    path1name = str(FileName) + ".png"
    kk = pyautogui.screenshot()
    kk.save(path1name)
    os.startfile(path1name)

#---- Time Function - Done

def TimeFunction():
    time = datetime.datetime.now().strftime("%H:%M")
    return time

#---- Date Function - Done

def DateFunction():
    date = datetime.date.today()
    return date

#---- Day Function - Done

def DayFunction():
    import datetime
    today = datetime.datetime.now().strftime("%A")

    Say(f"Today's Is : {today} .")

#---- Year Function - Done

def YearFunction():

    today = date.today()

    year = today.strftime("%Y")

    Say(f"This Is Year : {year} .")

#---- Dictionary Function - Done

def Dictionary(Word):

    Command = str(Word)

    Diction = PyDictionary()

    if 'synonym' in Command:
        Word = Command.replace("synonym of ","")
        synon = Diction.synonym(Word)
        Say(f"Synonym Of {Word} Is {synon} .")

    elif 'antonym' in Command:
        Word = Command.replace("antoynm of ","")
        anton = Diction.antonym(Word)
        Say(f"Antonym Of {Word} Is {anton} .")

    elif 'meaning' in Command:
        Word = Command.replace("meaning of ","")
        mean = Diction.meaning(Word)
        Say(f"The Meaning Of {Word} Is {mean} .")

#---- Translator Function - Done

def TRanslator():
    Say("What You Want To Translate ??")
    print("<< Speak In Hindi >>")
    line = Listen_Hindi()
    translate = Translator()
    result = translate.translate(line)
    uu = result.text
    Say(f"the translation for this line is {uu}")

#---- Map Automation Function - Done

def GoogleMaps(Place):

    Url_Place = "https://www.google.com/maps/place/" + str(Place)

    geolocator = Nominatim(user_agent="myGeocoder")

    location = geolocator.geocode(Place , addressdetails= True)

    target_latlon = location.latitude , location.longitude

    webbrowser.open(url=Url_Place)

    location = location.raw['address']

    target = {'city' : location.get('city',''),
                'state' : location.get('state',''),
                'country' : location.get('country','')}

    current_loca = geocoder.ip('me')

    current_latlon = current_loca.latlng

    distance = str(great_circle(current_latlon,target_latlon))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)


    Say(target)
    Say(f"Sir , {Place} iS {distance} Kilometre Away From Your Location . ")

#---- Battery Function. - Done

def Battery():

    import psutil

    def convertTime(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "%d:%02d:%02d" % (hours, minutes, seconds)

    battery = psutil.sensors_battery()

    Say("Battery percentage : ", battery.percent)
    Say("Power plugged in : ", battery.power_plugged)
    Say("Battery left : ", convertTime(battery.secsleft))

#---- Scroll Down Function. - Done

def ScrollDown():

    keyboard.press('pagedown')
    sleep(0.5)
    keyboard.press('pagedown')
    sleep(0.5)
    keyboard.press('pagedown')

#---- Scroll UP Function. - Done

def ScrollUp():

    keyboard.press('up')
    sleep(0.5)
    keyboard.press('up')
    sleep(0.5)
    keyboard.press('up')
    sleep(0.5)
    keyboard.press('up')

#---- vOICE Recording - Done.

def VoiceRecorder():

    Say("Starting The Voice Recorder.")

    import tkinter as tk
    import threading
    import pyaudio
    import wave

    class App():
        chunk = 1024 
        sample_format = pyaudio.paInt16 
        channels = 2
        fs = 44100  
        
        frames = []

        def __init__(self,master):
            self.isrecording = False
            self.button1 = tk.Button(main, text='rec',command=self.startrecording)
            self.button2 = tk.Button(main, text='stop',command=self.stoprecording)
        
            self.button1.pack()
            self.button2.pack()

        def startrecording(self):
            self.p = pyaudio.PyAudio()  
            self.stream = self.p.open(format=self.sample_format,channels=self.channels,rate=self.fs,frames_per_buffer=self.chunk,input=True)
            self.isrecording = True
            
            print('Recording......')
            t = threading.Thread(target=self.record)
            t.start()

        def stoprecording(self):
            self.isrecording = False
            print("  ")
            print('recording complete')
            print("  ")
            Say("Waht Should i Name the File ?")
            self.filename= Listen()
            self.filename = self.filename+".wav"
            wf = wave.open(self.filename, 'wb')
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.p.get_sample_size(self.sample_format))
            wf.setframerate(self.fs)
            wf.writeframes(b''.join(self.frames))
            wf.close()
            main.destroy()

        def record(self):
        
            while self.isrecording:
                data = self.stream.read(self.chunk)
                self.frames.append(data)

    main = tk.Tk()
    main.title('recorder')
    main.geometry('300x100')
    app = App(main)
    main.mainloop()

#---- Woflram Aplha API Function - Done

def Wolfram(query):
    
    api = "LWGWYQ-WQVK6X2XJL"

    requester = wolframalpha.Client(api)

    request = requester.query(query)

    try:
        
        answer = next(request.results).text

        Say(answer)

    except:

        Say("I am Really Sorry Sir. I Can Not Access The Answer!")

#---- Calulator  - Done

def Calculator(Problem):

    r = str(Problem)

    kk = Wolfram(r)

    Say(kk)

#---- Google Search Function - Done

def GoogleSearch(Topic):

    if 'how to' in Topic:
        Say("Getting Data From The Internet !")
        op = Topic.replace("jarvis","")
        max_result = 1
        how_to_func = search_wikihow(op,max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        Say(how_to_func[0].summary)

    else:
        import wikipedia as googleScrap
        query = Topic.replace("jarvis","")
        query = Topic.replace("google search","")
        query = Topic.replace("google","")
        query = Topic.replace("what is ","")
        query = Topic.replace("who is ","")
        Say("This Is What I Found On The Web!")
        pywhatkit.search(query)

        try:
            result = googleScrap.summary(query,2)
            Say(result)

        except:
            Say("No Speakable Data Available!")

#---- Wikipedia Function - Done

def Wikipedia(Topic):

    Topic = str(Topic).replace("what is ","")

    resd = wikipedia.summary(Topic,2)

    Say(f"According To My Research : {resd}")

#--- Space News - Done

def NasaNews():

    Say("Extracting News.......")

    ApiKey = "Mh2CXuG9rLTyIl0Djv8cRQvmEwOOf58heY00KFS9"

    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(ApiKey)

    Date = input("Enter Date In Year-Month-Day Format Like 2021-01-01 :")

    Params = {'date':str(Date)}
    
    r = requests.get(Url,params = Params)

    Data = r.json()

    Info = Data['explanation']

    Title = Data['title']

    Image_Url = Data['url']

    Image_r = requests.get(Image_Url)

    FileName = str(Date) + '.jpg'

    with open(FileName,'wb') as f:

        f.write(Image_r.content)

    img = Image.open(FileName)

    img.show()

    Say(f"Title : {Title} .")
    Say(f"Summary : {Info} .")

#---- YouTube Search Function - Done

def YouTubeSearch(Topic):
        Say("Ok Sir , Searching..")
        query = Topic.replace("youtube search","")
        url = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open_new_tab(url)
        pywhatkit.playonyt(Topic)

#---- Repeatme Function - Done

def RepeatMe():
    Say("What You Want Me To Repeat ?")
    rep = Listen()
    Say(f"You Said : {rep} .")
    Say("Thanks .")

#---- Jokes Function - Done

def Jokes():
    Joke = pyjokes.get_jokes(language='en')
    Say(Joke)

#---- Speedtest Function - Done

def SpeedTest():
    Say("Checking Your Internet Speed .")
    st = speedtest.Speedtest()
    dl = st.download()
    kk = int(dl/800000)
    up = st.upload()
    mk = int(up/800000)
    Say(f"Downloading speed is {kk} mbp s and uploading speed is {mk} mbp s , sir")

#--------------------------------------------------------------------------------------------------------------------------------------

#---- This Function Will Let Jarvis Understand Our Hindi.

def Listen_Hindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("          ")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='hi')
        print(f"Your Command :  {query}\n")

    except Exception as e:   
        return "None"
        
    return query.lower()

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

#---- This Function Will Help You To Verify a Function and Tell You A Query About Your Query

def FTasker(Tasks,Command):

    Tasks = str(Tasks)
    
    Command = str(Command)

    if "time" in Tasks:
        time = datetime.datetime.now().strftime("%H:%M")
        Say(time)

    elif "date" in Tasks:
        date = datetime.date.today()
        Say(date)

    elif "launch" in Tasks:
        LaunchWebsite(Command)

    elif "open" in Tasks:
        ApplicationOpener(Command)

    elif "note" in Tasks:
        NotesMaker()
    
    elif "type" in Tasks:
        TypeFunction()

    elif "trans" in Tasks:
        TRanslator()

    elif "day" in Tasks:
        DayFunction()

    elif "year" in Tasks:
        YearFunction()

    elif "temp" in Tasks:
        name = str(Command).replace("temperature in ","")
        name = str(name).replace("weather in ","")
        Temperature(name)

    elif "ss" in Tasks:
        Screenshot()

    elif "sys" in Tasks:
        SystemInfo()

    elif "in" in Tasks:
        ZoomIn()

    elif "out" in Tasks:
        ZoomOut()

    elif "scup" in Tasks:
        ScrollUp()

    elif "scdown" in Tasks:
        ScrollDown()

    elif "battery" in Tasks:
        Battery()

    elif "change" in Tasks:
        ChangeIp()

    elif "ipadd" in Tasks:
        IpAdd()

    elif "keybrd" in Tasks:
        Command_23 = str(Command).replace("press ","")
        PressKey(Command_23)

    elif "dict" in Tasks:
        Dictionary(Command)

    elif "locate" in Tasks:
        place = str(Command).replace("where is ","")
        place = str(place).replace("locate ","")
        GoogleMaps(place)

    elif "voice" in Tasks:
        VoiceRecorder()
    
    elif "calculate" in Tasks:
        cmd_12371283 = str(Command).replace("calculate ","")
        cmd_12371283 = str(cmd_12371283).replace("calculator ","")
        Calculator(cmd_12371283)

    elif "search" in Tasks:
        cmd_2342348 = str(Command).replace("google search ","")
        cmd_2342348 = str(cmd_2342348).replace("google ","")
        cmd_2342348 = str(cmd_2342348).replace("search ","")
        GoogleSearch(cmd_2342348)

    elif "wiki" in Tasks:
        realcmd = str(Command).replace("wikipedia ","")
        Wikipedia(realcmd)

    elif "alarm" in Tasks:
        os.startfile("My System\\Features\\Alarm.py")

    elif "space" in Tasks:
        NasaNews()

    elif "speed" in Tasks:
        SpeedTest()

    elif "joke" in Tasks:
        Jokes()

    elif "youtube" in Tasks:
        comnd = str(Command).replace("youtube search ","")
        YouTubeSearch(comnd)
