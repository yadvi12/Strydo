# importing the modules used in the program
import pyttsx3
import os
import subprocess
import datetime
import wikiquote
import time
import pyjokes
import winshell
import urllib.request
import re
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate') 
engine.setProperty('rate', 125)
print("                                   -------------------->>>>>>>>>>>>> STRYDO <<<<<<<<<<<<<---------------------")


# changing voice to male or female voice depending on the user's input
pyttsx3.speak("Greetings, this is strydo, a personal voice assistant made by yaadvi, which will be there for you everytime you need it. Tell me, you wanna talk to Ella or Scarlet?")
print("Ella or Scarlet: ", end = '')
speaker = input()
speaker = speaker.lower()
if ("ella" in speaker):
    engine.setProperty('voice', voices[1].id)
elif ("scarlet" in speaker):
    engine.setProperty('voice', voices[0].id)
else:
    print("Sorry, we couldn't recognize you ")
        



# Changing the greeting message depending on the time of the day
pyttsx3.speak("Hello my friend, I would like to know your good name?")
print("Your name please: ", end = '')
name = input()
hour = int(datetime.datetime.now().hour)
if hour>=0 and hour<12:
    pyttsx3.speak("Good Morning " + name + "  it's my pleasure to assist you!")
elif hour>=12 and hour<18:
    pyttsx3.speak("Good Afternoon " + name + "  i would love to help you!")
else:
    pyttsx3.speak("Good Evening " + name + "  i am glad you asked me for help!")





# writing conditions to help voice assistant perform different tasks depending on user's input
while True:
    print("What can i do for you: ", end='')

    p = input()
    p = p.lower()
    # print(p)
    # os.system(p)

    if ((("run" in p) or ("execute" in p) or ("use" in p) or ("open" in p) or ("start" in p) or ("launch" in p)) and ("chrome" in p or "browser" in p)):
        os.system("start chrome")
    elif ("quote" in p or "quotes" in p):
        pyttsx3.speak(wikiquote.quote_of_the_day())
        print(wikiquote.quote_of_the_day())
    elif ((("run" in p) or ("execute" in p) or ("use" in p) or ("open" in p) or ("start" in p) or ("launch" in p)) and ("media player" in p)):
        os.system("wmplayer")
    elif ((("see" in p) or ("tell" in p) or ("look" in p) or ("speak" in p) or ("find" in p)) and ("day" in p)):
        x = datetime.datetime.now()
        pyttsx3.speak("Today is " + x.strftime("%A"))
    elif ("empty recycle bin" in p):
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        pyttsx3.speak("Now your recycle bin is recycled.")
    elif ((("see" in p) or ("tell" in p) or ("look" in p) or ("speak" in p) or ("find" in p)) and ("month" in p)):
        x = datetime.datetime.now()
        pyttsx3.speak("The current month is" + x.strftime("%B"))
    elif ((("run" in p) or ("execute" in p) or ("use" in p) or ("open" in p) or ("start" in p) or ("launch" in p)) and (("vmware" in p) or ("VMware" in p))):
        os.system("cd C:\Program Files (x86)\VMware\VMware Player & vmplayer")
        
    elif ((("run" in p) or ("execute" in p) or ("use" in p) or ("open" in p) or ("see" in p) or ("start" in p) or ("launch" in p)) and ("security" in p)):
        os.system("start windowsdefender:")
    elif ((("run" in p) or ("execute" in p) or ("use" in p) or ("open" in p) or ("see" in p) or ("start" in p) or ("launch" in p)) and (("control-panel" in p) or ("control panel" in p))):
        os.system("start control")
    elif ((("run" in p) or ("execute" in p) or ("use" in p) or ("open" in p) or ("start" in p) or ("launch" in p)) and ("edge" in p)):
        os.system("start microsoft-edge:")
    elif ((("run" in p) or ("execute" in p) or ("use" in p) or ("open" in p) or ("show" in p) or ("see" in p) or ("start" in p) or ("launch" in p)) and (("mail" in p) or ("email" in p) or ("gmail" in p))):
        os.system("start outlookmail:")
    elif ((("run" in p) or ("execute" in p) or ("use" in p) or ("show" in p) or ("open" in p) or ("see" in p) or ("start" in p) or ("launch" in p)) and  ("calendar" in p)):
        os.system("start outlookcal:")
    elif ((("run" in p) or ("execute" in p) or ("use" in p) or ("open" in p) or ("start" in p) or ("launch" in p) or ("go" in p)) and ("store" in p)):
        os.system("start ms-windows-store:") 
    elif (("recorder" in p) or ("record" in p)):
        os.system("start ms-callrecording:")
    elif ((("look" in p) or ("show" in p) or ("tell" in p) or ("open" in p) or ("see" in p) or ("launch" in p) or ("start" in p) or ("use" in p)) and (("weather" in p) or ("temperature" in p) or ("climate" in p))):
        os.system("explorer bingweather:")
    elif ((("look" in p) or ("show" in p) or ("tell" in p) or ("open" in p) or ("see" in p) or ("launch" in p) or ("start" in p) or ("use" in p)) and (("maps" in p) or ("map" in p) or ("location" in p))):
        os.system("start bingmaps:")
    elif ((("run" in p) or ("execute" in p) or ("show" in p) or ("use" in p) or ("open" in p) or ("start" in p) or ("launch" in p)) and ("settings" in p or "setting" in p)):
        os.system("start ms-settings:")
    elif ((("run" in p) or ("execute" in p) or ("use" in p) or ("open" in p) or ("start" in p) or ("launch" in p) or ("talk" in p)) and ("skype" in p)):
        os.system("skype")
    elif ((("run" in p) or ("execute" in p) or ("use" in p) or ("open" in p) or ("start" in p) or ("launch" in p)) and ("vsc" in p or "visual" in p)):
        os.system("code .")
    elif ((("run" in p) or ("execute" in p) or ("use" in p) or ("open" in p) or ("start" in p) or ("launch" in p)) and ("atom" in p)):
        os.system("atom")
    elif ((("run" in p) or ("execute" in p) or ("use" in p) or ("open" in p) or ("start" in p) or ("launch" in p)) and ("editor" in p or "notepad" in p)):
        os.system("notepad")
    elif ((("run" in p) or ("execute" in p) or ("use" in p) or ("open" in p) or ("start" in p) or ("launch" in p)) and ("calculator" in p)):
        os.system("calc")
    elif ((("run" in p) or ("execute" in p) or ("use" in p) or ("open" in p) or ("start" in p) or ("launch" in p) or ("take" in p) or ("click" in p)) and (("camera" in p) or ("selfie" in p))):
        subprocess.run("start microsoft.windows.camera:", shell=True)
    elif ("why you came to world" in p):
            pyttsx3.speak("Thanks to Yaadvi. Further It's a secret")
    elif 'joke' in p:
            pyttsx3.speak(pyjokes.get_joke())
    elif ((("run" in p) or ("execute" in p) or ("use" in p) or ("open" in p) or ("start" in p) or ("launch" in p)) and ("whatsapp" in p)):
        os.system("start chrome https://web.whatsapp.com/")
    
    elif ((("hear" in p) or ("play" in p) or ("sing" in p) or ("start" in p) or ("listen" in p)) and ("baby shark" in p)):
        os.system("start chrome https://www.youtube.com/watch?v=XqZsoesa55w")
    elif ("youtube" in p):
        os.system("start chrome https://www.youtube.com/")
    elif ("quora" in p):
        os.system("start chrome www.quora.com")
    elif ("facebook" in p):
        os.system("start chrome https://www.facebook.com/")
    elif ("medium" in p):
        os.system("start chrome https://medium.com/")
    elif ("twitter" in p):
        os.system("start chrome https://twitter.com/")
    elif ("linkedin" in p):
        os.system("start chrome https://www.linkedin.com/")
    elif ("github" in p):
        os.system("start chrome https://github.com/")
    elif ("open stackoverflow" in p):
        pyttsx3.speak("Here you go to Stack Over flow,Happy coding!")
        os.system("start chrome stackoverflow.com") 
    elif ("ssh" in p or "putty" in p):
        pyttsx3.speak("Tell us the I P address of the host system: ")
        print("IP Address of host: ", end= '')
        IP = input()
        os.system("putty -ssh " + IP + "@host")
    elif ("remote desktop connection" in p):
        os.system("start mstsc")
    elif ((("run" in p) or ("execute" in p) or ("open" in p) or ("use" in p) or ("start" in p) or ("launch" in p) or ("draw" in p)) and (("paint" in p) or ("draw" in p))):
        os.system("Mspaint")
    elif ((("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) or ("show" in p) or ("launch" in p)) and (("recycle bin" in p) or ("bin" in p) or ("dustbin" in p))):
        os.system("start shell:RecycleBinFolder")
    elif ((("look" in p) or ("show" in p) or ("tell" in p) or ("open" in p) or ("see" in p) or ("launch" in p)) and ("date" in p)):
        os.system("DATE /T")
    elif ((("set" in p) or ("change" in p) or ("modify" in p) or ("settings" in p) or ("alter" in p) or ("adjust" in p)) and ("date" in p)):
        os.system("DATE")
    elif ((("look" in p) or ("show" in p) or ("open" in p) or ("tell" in p) or ("see" in p) or ("launch" in p)) and ("time" in p)):
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        pyttsx3.speak("the time is" + strTime)
    elif ((("set" in p) or ("change" in p) or ("modify" in p) or ("settings" in p) or ("alter" in p) or ("adjust" in p)) and ("time" in p)):
        os.system("TIME")
    elif ("thank you" in p or "thanks" in p):
        pyttsx3.speak("I know you would help me if I needed it, I am glad to do the same for you")
    elif ("why" in p and ("call" in p or "name" in p) and "strydo" in p):
        pyttsx3.speak("S is for serious, not always joking, T is for treasure, that of your friendship, R is for rapport, friends seek you, Y is for yes, always open to new possibilities,D is for decisive, especially when it counts,O is for objective, always impartial")
        
    elif ((("pretty" in p) or ("good" in p) or ("beautiful" in p) or ("helpful" in p) or ("amazing" in p) or ("smart" in p) or ("great" in p) or ("gorgeous" in p)) and ("you" in p)):
        pyttsx3.speak("After hearing what you just said, I realized that honest people still do exists!")
    elif ((("pretty" in p) or ("good" in p) or ("beautiful" in p) or ("helpful" in p) or ("amazing" in p) or ("smart" in p) or ("great" in p) or ("gorgeous" in p)) and (("i" in p) or ("me" in p))):
        pyttsx3.speak("You're even more beautiful on the inside than you are on the outside, You are a gift to those around you")
    elif ((("run" in p) or ("execute" in p) or ("open" in p) or ("use" in p) or ("start" in p) or ("launch" in p)) and ("word" in p)):
        os.system("start winword")
    elif ((("run" in p) or ("execute" in p) or ("open" in p) or ("use" in p) or ("start" in p) or ("launch" in p)) and ("excel" in p)):
        os.system("start excel")
    elif ((("run" in p) or ("execute" in p) or ("open" in p) or ("use" in p) or ("start" in p) or ("launch" in p)) and ("powerpoint" in p)):
        os.system("start powerpnt")
    elif ((("run" in p) or ("execute" in p) or ("open" in p) or ("use" in p) or ("start" in p) or ("launch" in p)) and (("device-manager" in p) or ("device manager" in p))):
        os.system("start devmgmt.msc")
    elif (("log off" in p or "sign out" in p) and ("system" in p or "computer" in p or "PC" in p or "pc" in p or "laptop" in p)):
        pyttsx3.speak("Make sure all the application are closed before sign-out")
        time.sleep(5)
        subprocess.call(["shutdown", "/l"])
    elif ("will you be my gf" in p or "will you be my bf" in p):   
        pyttsx3.speak("Sorry dear! but i can't")
    
    elif ("file explorer" in p):
        os.system("c:\windows\explorer.exe")
    elif ("whats up" in p):
        pyttsx3.speak("Just doing my thing")
    elif (("hibernate" in p or "sleep" in p) and ("system" in p or "computer" in p or "PC" in p or "pc" in p or "laptop" in p)):
        pyttsx3.speak("Hibernating")
        subprocess.call("shutdown /i /h")
    elif (("restart" in p) and ("system" in p or "computer" in p or "PC" in p or "pc" in p or "laptop" in p)):
        pyttsx3.speak("Restarting Your PC")
        subprocess.call(["shutdown", "/r"])
    elif (("shutdown" in p) and ("system" in p or "computer" in p or "PC" in p or "pc" in p or "laptop" in p)):
        pyttsx3.speak("Hold On a Sec! Your system is on its way to shut down")
        subprocess.call('shutdown /p /f')
    elif (("how are you" in p) or ("how r u" in p) or ("How are you" in p)):
        pyttsx3.speak("I am perfectly fine, Hope you are good as well!")
    elif ((("music" in p) or ("movie" in p) or ("song" in p) or ("bhajan" in p) or ("recipe" in p)) and (("play" in p) or ("listen" in p) or ("watch" in p))):
        pyttsx3.speak("voila! here you go")
        value=str(p)
        link = urllib.request.urlopen("https://www.youtube.com/results?search_query=" +(str(re.sub("[ ]", "+", value))))
        videolink = re.findall(r"watch\?v=(\S{11})", link.read().decode())
        finalwebsite=('https://www.youtube.com/watch?v=' + videolink[0])
        webbrowser.open_new(finalwebsite)
    elif (("exit" in p) or ("quit" in p) or ("close" in p) or ("goodbye" in p) or ("terminate" in p) or ("bye" in p) or ("leave" in p)):
        pyttsx3.speak("Goodbyes are not forever, are not the end; it simply means I’ll miss you until we meet again.")
        break   
    else:
        pyttsx3.speak("Do you want me to search your query on the internet?")
        print("yes or no: ", end ='')
        response = input()
        if ("yes" in response or "y" in response or "Yup" in response):
            pyttsx3.speak("Here you go!")
            query = str(p)
            webbrowser.open('http://www.google.com/search?btnG=1&q=%s'%query)
        else:
            pyttsx3.speak("Sorry! we didn't recognize what you want, Can you be more specific please?")
