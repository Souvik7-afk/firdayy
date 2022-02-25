#F.R.I.D.A.Y.Y- The handy assistant for your regular use :"))


import PySimpleGUI as sg
from tkinter.constants import TRUE
import datetime
import time
import psutil
import pywhatkit
import requests
import json
import smtplib
import bs4
import wikipedia
import webbrowser
from random import choice
import os
from tkinter import *
from pywhatkit.misc import search
import cv2
import pyjokes


def Weather(timeing):                           #weather fumction
    try:
        with open("Credentials.json") as f:            #your weather api is stored in Credentials.json file
            contents = json.load(f)
            key = contents["OpenWeatherKey"]
            Place = contents["City"]
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "q=" + Place + "&APPID=" + key + "&units=metric"
        response = requests.get(complete_url)     
        x = response.json()                                #--to know more bout .json use this link- https://www.geeksforgeeks.org/response-json-python-requests/ 
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_temp = current_temperature
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            print(timeing + Place + ":")
            print(" Temperature (Celsius) = " + str(current_temp) +
                  "\n Humidity (Percentage) = " + str(current_humidiy) + "\n Description = " + str(weather_description))
            Audfile = open("cookies.txt", "a")                               #cookies file is similar to browser history. keeps track of all chatbot actions
            querytime = (datetime.datetime.now().ctime())
            Audfile.writelines(querytime + "-(User GETS WEATHER REPORT!!!) \n")   
            Audfile.close()
        else:
            print("Nilanjana : Please check your city in the settings as this is invalid.")
            Audfile = open("cookies.txt", "a")
            querytime = (datetime.datetime.now().ctime())
            Audfile.writelines(querytime + "-(User'S CITY IS INVALID!!!) \n")
            Audfile.close()
    except:
        print("Nilanjana : I am having a problem in getting live weather please check your network-Connection.")
        Audfile = open("cookies.txt", "a")
        querytime = (datetime.datetime.now().ctime())
        Audfile.writelines(querytime + "-(Connection failed WITH OPENWEATHERMAP.ORG!!!) \n")
        Audfile.close()


def stocks(tickers):                                      #search for stocks news
    try:
        tickers = tickers.upper()
        link = 'https://www.moneycontrol.com/markets/global-indices/'+tickers+'?p='+tickers
        url = requests.get(link)
        soup = bs4.BeautifulSoup(url.text, features="html.parser")
        price = soup.find_all("div", {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[
            0].find('span').text
        print("Current pricing of Stock for "+tickers+" is: "+price)
        Audfile = open("cookies.txt", "a")
        querytime = (datetime.datetime.now().ctime())
        Audfile.writelines(querytime + "-(User GETS STOCK PRICES FOR "+ tickers +"!!!) \n")
        Audfile.close()
    except:
        print("Nilanjana : I am having a problem in getting Stock Prices please check your network-Connection")
        Audfile = open("cookies.txt", "a")
        querytime = (datetime.datetime.now().ctime())
        Audfile.writelines(querytime + "-(Connection failed TO GET STOCK PRICES!!!) \n")
        Audfile.close()


def Breifing(title, text):                                                             #news function
    str = 'general business science health technology entertainment sports'   #keywords that can be used to search news
    with open("Credentials.json") as f:   
        contents = json.load(f)
        JNews = contents["NewsApiKey"]                              
        country = contents["Country"]
    headers = {'Authorization': JNews}
    top_headlines_url = 'https://newsapi.org/v2/top-headlines'

    if title == 'Morning Briefing':                                     #pop up of morning news
        sg.theme('DarkBlue13')     
        layout = [[sg.Text(text)],
                  [sg.Output(size=(45, 20), font=('Helvetica 10'))],
                  [sg.Button('GET NEWS'), sg.Button('EXIT')]]
        window = sg.Window(title, layout, no_titlebar=True, keep_on_top=True)
        while True:     
            event, value = window.read()
            if event in (sg.WIN_CLOSED, 'EXIT'):            
                break
            if event == 'GET NEWS':                           #get-news button of news search dialogue box
                try:
                    splits = str.split()
                    for split in splits:
                        print("\n" + split.upper() + ":--")
                        headlines_payload = {
                            'category': split, 'country': country}
                        open_news_page = requests.get(
                            url=top_headlines_url, headers=headers, params=headlines_payload).json()
                        article = open_news_page["articles"]
                        results = []
                        Audfile = open("cookies.txt", "a")
                        querytime = (datetime.datetime.now().ctime())
                        Audfile.writelines(querytime + "-(Connection ESTABLISHED WITH NEWSAPI.ORG!!!) \n")
                        Audfile.close()
                        for ar in article:
                            results.append(ar["title"])
                        for i in range(len(results)):
                            print(i + 1, '.', results[i])
                except:
                    print("Nilanjana : Something went wrong!!!" +
                          "\nPlease check if you have a good network Connection and have given a valid \ncategory and location.")
                    Audfile = open("cookies.txt", "a")
                    querytime = (datetime.datetime.now().ctime())
                    Audfile.writelines(
                        querytime + "-(Connection failed WITH NEWSAPI.ORG!!!) \n")
                    Audfile.close()
                    continue
        window.close()
        event = window.read()
        return event != 'OK'
    else:                                                                   #when we search for news in chat box directly
        sg.theme('Darkgreen3')
        window = sg.Window(title,
                           [[sg.Text(text)],
                            [sg.Output(size=(46, 20), font=('Helvetica 10'))],
                               [sg.Multiline(size=(28, 1), enter_submits=TRUE, key='-NEWS-', do_not_clear=False),
                                sg.Button('GET NEWS', bind_return_key=True),
                                sg.Button('EXIT')]], no_titlebar=True, keep_on_top=True)
        while True:     
            event, value = window.read()
            if event in (sg.WIN_CLOSED, 'EXIT'):            
                break
            if event == 'GET NEWS':
                country = value['-NEWS-'].rstrip()
                try:
                    splits = str.split()
                    for split in splits:
                        print("\n" + split.upper() + ":--")
                        headlines_payload = {
                            'category': split, 'country': country}
                        open_news_page = requests.get(
                            url=top_headlines_url, headers=headers, params=headlines_payload).json()
                        article = open_news_page["articles"]
                        results = []
                        Audfile = open("cookies.txt", "a")
                        querytime = (datetime.datetime.now().ctime())
                        Audfile.writelines(querytime + "-(Connection ESTABLISHED WITH NEWSAPI.ORG!!!) \n")
                        Audfile.close()
                        for ar in article:
                            results.append(ar["title"])
                        for i in range(len(results)):
                            print(i + 1, '.', results[i])
                except:
                    print("Nilanjana : Something went wrong!!!" +
                          "\nNilanjana : Please check if you have a good \nnetwork Connection and have given a valid \ncategory and location.")
                    Audfile = open("cookies.txt", "a")
                    querytime = (datetime.datetime.now().ctime())
                    Audfile.writelines(
                        querytime + "-(Connection failed WITH NEWSAPI.ORG!!!) \n")
                    Audfile.close()
                    continue
        window.close()
        event = window.read()
        return event != 'OK'


def Settings():                                             #settings button on top 
    sg.theme('darkteal6')
    with open("Credentials.json") as f:
        contents = json.load(f)
        User = contents["User"]
        NewsApiKey = contents["NewsApiKey"]
        OpenWeatherKey = contents["OpenWeatherKey"]
        Country = contents["Country"]
        City = contents["City"]
        Outputsc = contents["Outputscreensize"]
        Inputbr = contents["Inputbarsize"]
    layout = [[sg.Text('Settings', font='Default 16')],
              [sg.Text('Your-Details:--', font='Default 12')],
              [sg.Text('Enter your information and Api-Keys.', font='Default 10')],
              [sg.T('User-Name:', size=(13, 1)), sg.Input(
                  User, key='-User-', size=(34, 1))],
              [sg.T('NewsApiKey:', size=(13, 1)), sg.Input(
                  NewsApiKey, key='-NewsApi-', size=(34, 1))],
              [sg.T('OpenWeatherMap:', size=(14, 1)), sg.Input(
                  OpenWeatherKey, key='-OpenWeather-', size=(33, 1))],
              [sg.T('Current-Country:', size=(13, 1)), sg.Input(
                  Country, key='-Country-', size=(34, 1))],
              [sg.T('Current-City:', size=(13, 1)), sg.Input(
                  City, key='-City-', size=(34, 1))],
              [sg.Text('GUI-Customization:--', font='Default 12')],
              [sg.Text('Enter only in Numbers to adjust the UI screen size.', font='Default 10')],
              [sg.T('Output-Screen:', size=(13, 1)), sg.Input(
                  Outputsc, key='-Outsc-', size=(34, 1))],
              [sg.T('Input-bar:', size=(13, 1)), sg.Input(
                  Inputbr, key='-Inbr-', size=(34, 1))],
              [sg.Button('Save'), sg.Button('Exit')]]
    window = sg.Window('Settings', layout, no_titlebar=True, keep_on_top=True)

    while True:  
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Save':                        #saving the data in settings
            User = values['-User-']
            newsapikey = values['-NewsApi-']
            weatherkey = values['-OpenWeather-']
            Country = values['-Country-']
            City = values['-City-']
            Outputsc = values['-Outsc-']
            Inputbr = values['-Inbr-']
            dictionary = {
                "!CAUTION!": "PLEASE REFRAIN from TAMPERING with the BELOW DATA!!!",
                "User": User,
                "NewsApiKey": newsapikey,
                "OpenWeatherKey": weatherkey,
                "Country": Country,
                "City": City,
                "Outputscreensize": Outputsc,
                "Inputbarsize": Inputbr
            }
            json_object = json.dumps(dictionary, indent=4)
            with open("Credentials.json", "w") as outfile:
                outfile.write(json_object)
            break
    window.close()
    event = window.read()
    return event != 'OK'


def send_an_email(from_address, to_address, subject, message_text, password):            #send email
    try:
        Nilanjana_mail = '\n \n \n \n                                                        ---This message was sent to you by Nilanjana  :-)'
        full_message = "{0} {1}".format(message_text, Nilanjana_mail)
        email_message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                """ % (from_address, to_address, subject, full_message)
        # Use port 587 or 465 using SMTP_SSL
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()    # start TLS for security
        s.login(from_address, password)    # Authentication to your account
        s.sendmail(from_address, to_address,
                   email_message)    # sending the email
        Audfile = open("cookies.txt", "a")
        querytime = (datetime.datetime.now().ctime())
        Audfile.writelines(querytime + "-(User SUCCESSFULLY SENT AN EMAIL!!!) \n")
        Audfile.close()
        s.quit()    # terminating the session
    except:
        sg.popup("Please check your network Connection and have turned 'on' Less secure app access in 'security' section in your Google Account Settings.")
        Audfile = open("cookies.txt", "a")
        querytime = (datetime.datetime.now().ctime())
        Audfile.writelines(
            querytime + "-(User failed TO SEND AN EMAIL!!!) \n")
        Audfile.close()

def gmail():                                                              #email dialogue box
    sg.theme('bluemono')
    layout = [[sg.Text('Send an Email', font='Default 15')],
              [sg.T('From:', size=(8, 1)), sg.Input(
                  key='-EMAIL FROM-', size=(35, 1))],
              [sg.T('To:', size=(8, 1)), sg.Input(
                  key='-EMAIL TO-', size=(35, 1))],
              [sg.T('Subject:', size=(8, 1)), sg.Input(
                  key='-EMAIL SUBJECT-', size=(35, 1))],
              [sg.T('Mail login information', font='Default 14')],
              [sg.T('Password:', size=(8, 1)), sg.Input(
                  password_char='*', key='-PASSWORD-', size=(35, 1))],
              [sg.Multiline('Type your message here',
                            size=(44, 10), key='-EMAIL TEXT-')],
              [sg.Button('Send')]]
    window = sg.Window('Send An Email', layout)

    while True:  
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Discard'):
            break
        if event == 'Send':
            send_an_email(from_address=values['-EMAIL FROM-'],
                          to_address=values['-EMAIL TO-'],
                          subject=values['-EMAIL SUBJECT-'],
                          message_text=values['-EMAIL TEXT-'],
                          password=values['-PASSWORD-'])
            continue
        window.close()
        event = window.read()
        return event != 'OK'


def digiclock():
    #speak("launching the digital clock")
    from tkinter import Label, Tk 
    import time
    app_window = Tk() 
    app_window.title("Digital Clock") 
    app_window.geometry("420x150") 
    app_window.resizable(1,1)

    text_font= ("Boulder", 68, 'bold')
    background = "#f2e750"
    foreground= "#363529"
    border_width = 25

    label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
    label.grid(row=0, column=1)

    def digital_clock():
        #speak("opening digital clock window") 
        time_live = time.strftime("%H:%M:%S")
        label.config(text=time_live) 
        label.after(200, digital_clock)

    digital_clock()
    app_window.mainloop() 


def power_check():
    
    import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if percent <= 40 and plugged!=True:
 

    from pynotifier import Notification

    Notification(
        title="Battery Low",
        description=str(percent) + "% Battery remain!!",
        duration=6,  # Duration in seconds
        
    ).send()


def openapps(term):
    if "NOTEPAD" in term:
        os.startfile("C:\\Windows\\System32\\notepad.exe")
    elif "COMMAND PROMPT" or "CMD" in term:
        os.system("start cmd")
    else:
        print("can not help  you !!!")


with open("Credentials.json") as f:
    contents = json.load(f)
    LoadOutput = contents["Outputscreensize"]
    LoadInput = contents["Inputbarsize"]
sg.theme('DarkTeal10')                                             # gives window a spiffy set of colors
sg.set_options(element_padding=(4,4))
menu_def = [['&MENU ', ['&Settings', 'E&xit']],                                #top buttons creation(menu, about us) 
            ['&ABOUT US', [ '&Our Website']], ]
layout = [[sg.Menu(menu_def, tearoff=False)],
          [sg.Text('                                                                                                                                            Nilanjana                                                                                                                                        ', size=(135,1))],
          [sg.Output(size=(LoadOutput, 35), font=('Helvetica 13'))],
          [sg.Multiline(size=(LoadInput, 2), enter_submits=True, key='-QUERY-', do_not_clear=False),
           sg.Button('ENTER',size=(11,2), bind_return_key=True)]]
window = sg.Window('Nilanjana GUI', layout, location=(0,0) ,icon=r'icon/Nilanjana.ico', font=(                 
    'Helvetica', ' 13'), default_button_element_size=(8, 2)).Finalize()
window.maximize()

print("Nilanjana : Welcome sir")
Audfile = open("cookies.txt", "a")
querytime = (datetime.datetime.now().ctime())
Audfile.writelines(querytime + "-(User ACTIVATED Nilanjana AND INITIALIZED RELATED PROCESSES!!!) \n")
Audfile.close()

hour = int(datetime.datetime.now().hour)              #-----general function, always work
if hour >= 0 and hour < 12:
    timeing = "Nilanjana : Good morning, here is the current weather in "
    Weather(timeing)
    Breifing('Morning Briefing', 'Morning News Headlines')     #only morning news will pop up
elif hour >= 12 and hour < 18:
    timeing = "Nilanjana : Good afternoon, here is the current weather in "
    Weather(timeing)
else:
    timeing = "Nilanjana : Good evening, here is the current weather in "
    Weather(timeing)
print("Functionalities Currently available : ")
print("Salutations, Date/Time, Wikipedia search, Current news, Stocks update, Send email, Goodbye")

if __name__ == '__main__':                              #----------DRIVER CODE STARTS
    while True:     
        event, value = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):   # quit if exit button or X                #exit at top right
            Audfile = open("cookies.txt", "a")
            querytime = (datetime.datetime.now().ctime())
            Audfile.writelines(querytime + "-(User TERMINATED Nilanjana AND ALL IT'S RELATED PROCESSES!!!) \n")
            Audfile.close()
            print("\nNilanjana: Goodbye sir hope you have a nice day :-)")
            time.sleep(4)
            break

        if event == 'ENTER':                                                #chatbox at bottom
            # THE START OF THE RENDER-WORD ENGINE (C) Epicalable
            que = value['-QUERY-'].rstrip()  # Your input here
            query = (que.upper())
            Audfile = open("cookies.txt", "a")
            querytime = (datetime.datetime.now().ctime())
            str = (querytime + ": " + que.capitalize() + "\n")
            Audfile.write(str)
            with open("Credentials.json") as f:
                contents = json.load(f)
                User = contents["User"]
                print("\n" + User + ": {}".format(que.capitalize()))
                with open("Dataset.json") as f:
                    data = json.load(f)
                    for word in data['intents']:                      #this will generate output according to dictionary in Dataset.json
                        if word['tags'] in query:
                            print(choice(word["response"]))
                            break
                #-------------------- THE END OF THE RENDER-WORD ENGINE . from here, network search starts--------------------
                    else:
                        if "DATE" in query or "TIME" in query:
                            x = datetime.datetime.now()
                            print("Nilanjana : The Date and Time is ",x," respectively sir.")
                            continue

                        elif "WIKIPEDIA" in query or "WIKI" in query:
                            query = query.replace('WIKI', "")
                            query = query.replace('WIKIPEDIA', "")
                            try:
                                print(wikipedia.summary(query))
                                Audfile = open("cookies.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(querytime + "-(Connection ESTABLISHED WITH WIKIPEDIA!!!) \n")
                                Audfile.close()
                            except:
                                #print(".")
                                print(
                                    "Nilanjana : I am having a problem in getting wikipedia please check your network-Connection.")
                                Audfile = open("cookies.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(querytime + "-(Connection failed WITH WIKIPEDIA!!!) \n")
                                Audfile.close()
                            continue

                        elif "WHAT IS" in query or "WHO IS" in query:
                            query = query.replace('WHAT', "")
                            query = query.replace('IS', "")

                            query = query.replace('WHO', "")
                            query = query.replace('IS', "")
                            try:
                                print(wikipedia.summary(query))
                                Audfile = open("cookies.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(querytime + "-(Connection ESTABLISHED WITH WIKIPEDIA!!!) \n")
                                Audfile.close()
                            except:
                                print(
                                    "Nilanjana : I am having a problem in getting wikipedia please check your network-Connection")
                                Audfile = open("cookies.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(querytime + "-(Connection failed WITH WIKIPEDIA!!!) \n")
                                Audfile.close()
                            continue

                        elif "NEWS ABOUT" in query or "NEWS ON" in query:
                            query = query.replace('NEWS ', "")
                            query = query.replace('ABOUT ', "")
                            query = query.replace('ON ', "")
                            try:
                                with open("Credentials.json") as f:
                                    contents = json.load(f)
                                    JNews = contents["NewsApiKey"]
                                headers = {'Authorization': JNews}
                                everything_news_url = 'https://newsapi.org/v2/everything'
                                everything_payload = {
                                    'q': query, 'language': 'en', 'sortBy': 'publishedAt'}
                                open_news_page = requests.get(
                                    url=everything_news_url, headers=headers, params=everything_payload).json()
                                article = open_news_page["articles"]
                                results = []
                                Audfile = open("cookies.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(
                                    querytime + "-(Connection ESTABLISHED WITH NEWSAPI.ORG!!!) \n")
                                Audfile.close()
                                for ar in article:
                                    results.append(ar["title"])
                                for i in range(len(results)):
                                    print(i + 1,'.', results[i])
                            except:
                                print(
                                    "Nilanjana : Something went wrong please check if you have a good network Connection.")
                                Audfile = open("cookies.txt", "a")
                                querytime = (datetime.datetime.now().ctime())
                                Audfile.writelines(
                                    querytime + "-(Connection failed WITH NEWSAPI.ORG!!!) \n")
                                Audfile.close()
                                continue

                        elif "HEADLINES" in query:
                            Breifing('News Headlines', 'Current Headlines(Enter country abbreviation in given field)')

                        elif "NEWS" in query:
                            Breifing('News Headlines', 'Current Headlines(Enter country abbreviation in given field)')
                        
                        elif "STOCKS" in query or "STOCK PRICE" in query:
                            query = query.replace('GET ME ', "")
                            query = query.replace('PRICE ', "")
                            query = query.replace('PRICES ', "")
                            query = query.replace('STOCK ', "")
                            query = query.replace('STOCKS ', "")
                            query = query.replace('FOR ', "")
                            query = query.replace('ON ', "")
                            stocks(tickers=query.upper())

                        elif "SEND AN EMAIL" in query or "EMAIL" in query:
                            gmail()


                        elif "DIGITAL CLOCK" in query:
                            try:
                                digiclock() 
                            except:
                                print("")


                        elif "GOOGLE SEARCH" in query:
                            query=query.replace("GOOGLE SEARCH","")
                            pywhatkit.search(query) 


                        elif "YOUTUBE SEARCH" in query:
                            query=query.replace("YOUTUBE SEARCH","")
                            result = "https://www.youtube.com/results?search_query=" + query
                            webbrowser.open(result)
                            pywhatkit.playonyt(query) 


                        elif "IP ADRESS" in query:
                            ip=requests.get("https://api.ipify.org").text 
                            print("Your IP Adress is: ",ip) 


                        elif "WEBSITE" in query:
                            query=query.replace("WEBSITE","")
                            webbrowser.open(query.lower()) 


                        elif "OPEN" in query:
                            openapps(query)   

                       


                        elif query == "GOODBYE":
                            Audfile = open("cookies.txt", "a")
                            querytime = (datetime.datetime.now().ctime())
                            Audfile.writelines(querytime + "-(User TERMINATED Nilanjana AND ALL IT'S RELATED PROCESSES!!!) \n")
                            Audfile.close()
                            print("Nilanjana : Goodbye sir hope you have a nice day :-)")
                            time.sleep(4)
                            break 
                            

                        else:
                            print(
                                "Nilanjana : I did not understand you, as you can see i am still evolving :-)")
                            Audfile = open("cookies.txt", "a")  
                            Audfile.write("ERROR 404 (FALLBACK)!!! \n")
                            Audfile.close() 



      #------------these are for top button functions(settings, our website)--------------

        elif event == 'Settings':           
            Settings()

        

        
        elif event == 'Our Website':
            webbrowser.open("https://www.newsmusk.com/", new=1)

    

window.close()

