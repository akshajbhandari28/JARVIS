import smtpd
import smtplib
import sys
import speedtest
import pyaudio
import pyjokes
import speech_recognition
from playsound import playsound
import pyautogui
import selenium
from selenium import webdriver
import pyttsx3
import wikipedia
import webbrowser
import os
import requests, json
import requests
import bs4
from selenium.webdriver.common.by import By
from os import startfile
from pyautogui import click
from keyboard import write
from time import sleep
import time
from plyer import notification
import datetime
import random
from twilio.rest import Client
import number
from email.message import EmailMessage
import ssl
from PIL import Image
from yahoo_fin.stock_info import *
import yahoo_fin
from gnewsclient import gnewsclient
import openai


strTime = datetime.datetime.now().strftime("%H:%M:%S")


res = yahoo_fin.requests.get('https://google.com/search?q=' + '')
api_key = "API_KEY"
ow_url = "http://api.openweathermap.org/data/2.5/weather?"
city = 'delhi'
call_url = ow_url + "appid=" + api_key + "&q=" + city
response = yahoo_fin.requests.get(call_url)
data = response.json()

if data["cod"] != "404":
    city_res = data["main"]

    current_temperature = city_res["temp"]

    current_pressure = city_res["pressure"]

current_humidity = city_res["humidity"]

wthr = data["weather"]
weather_description = wthr[0]["description"]
current_temperature = round(current_temperature - 273)
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("good morning boss!")
    elif 12 <= hour < 18:
        speak("good after noon boss")
    else:
        speak("good evening boss")
    speak('all systems for work will be ready in just a minute')
def system():
    speak(f'''the temperature outside is {current_temperature} and the time is {strTime} ''')
    sleep(1)
    speak('''all systems are up and running now''')


def takeCommand():

    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone(device_index=0) as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: , {query}\n")

    except Exception as e:
        print(e)
        speak("I couldn't catch you boss")
        print("I couldn't catch you boss \n")
        return "none"
    return query


if __name__ == '__main__':
    wishMe()
    system()
    while True:
        query = takeCommand().lower()

        if ' search wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)
        elif "search youtube" in query:
            driver = webdriver.Chrome(
                r'C:/Users/Asus/PycharmProjects/pythonProject/chromedriver_win32/chromedriver.exe')
            query = query.replace("search youtube", "")
            speak(f'searching youtube, {query}')
            driver.get(f'https://www.youtube.com/results?search_query={query}')
        elif "search google" in query:
            driver = webdriver.Chrome(
                r'C:/Users/Asus/PycharmProjects/pythonProject/chromedriver_win32/chromedriver.exe')
            query = query.replace("search google", "")
            speak(f'searching google {query}')
            driver.get(f'https://www.google.com/search?q={query}')
        elif "open github" in query:
            speak('opening github')
            webbrowser.open("github.com")
        elif "play music" in query:
            music_dir = 'C:\\Users\\Asus\\Music\\'
            songs = os.listdir(music_dir)
            speak('playing Shape of you by Ed Sheren')
            os.startfile(os.path.join(music_dir, songs[1]))
        elif "the time" in query:
            speak(f"the time is {strTime}")
        elif 'thank you jarvis' in query:
            speak('its a pleasure serving you sir')
        elif "join classes" in query:
            speak('opening microsoft teams')
            teamsPath = "C:\\Users\\Asus\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart Teams.exe"
            os.startfile(teamsPath)
        elif "update graphic drivers" in query:
            GeForceExperiencePath = "C:\\Program Files\\NVIDIA Corporation\\NVIDIA GeForce Experience\\NVIDIA GeForce Experience.exe"
            os.startfile(GeForceExperiencePath)
            sleep(10)
            click(x=251, y=62)
        elif "open wikipedia" in query:
            webbrowser.open('wikipedia.org')
            speak('opening wikipedia')
        elif 'open spotify' in query:
            spotifyPath = 'C:\\Users\\Asus\\AppData\\Roaming\\Spotify\\Spotify.exe'
            speak('opening spotify')
            os.startfile(spotifyPath)
        elif 'who are you' in query:
            speak('I am Jarvis i was made by Akshaj sir on 10th june 2022 and he is my boss')
        elif 'what can you do' in query:
            speak(
                'I can open google, youtube, github, play music, tell you the time, weather, set reminders, alarms, play a game, send sms, change the volume and a lot more!!')
        elif 'i will talk to you later' in query or 'bye' in query:
            hour_rn = datetime.datetime.now().hour
            if 0 <= hour_rn < 12:
                speak('have a good day boss, i will be waiting for you')
                break
            elif 12 <= hour_rn < 18:
                speak('good evening boss, call me when ever ')
                break
            else:
                speak('good night boss')
                break
        elif 'the best person in the world' in query:
            speak('i searched wikipedia and it shows that Akshaj sir is the best person in the world')
        elif 'how is your day going' in query:
            speak('a lot better now that i am able to talk with you')
        elif 'weather' in query:
            print(" Temperature (in Celsius) = " +
                  str(current_temperature) +
                  "\n atmospheric pressure (in hPa unit) = " +
                  str(current_pressure) +
                  "\n humidity (in percentage) = " +
                  str(current_humidity) +
                  "\n description = " +
                  str(weather_description))
            speak(
                f'the temperature outside is,{current_temperature} celsius,atmospheric pressure (in hPa unit) is {current_pressure}, humidity is {current_humidity} percent, and it is {weather_description} outside ')
        elif 'remind me to' in query:
            query = query.replace("remind me to", "", )
            speak('how often should i remind you?')
            how_often = int(input("enter an integer here: "))
            while True:
                notification.notify(
                    title='REMINDER!!',
                    message=f"{query}",
                    app_icon="C:\\Users\\Asus\\Desktop\\icon.ico",
                    timeout=10
                )
                time.sleep(how_often)
        elif 'set a reminder' in query:
            query = query.replace("set a reminder", "")
            speak("when should i remind you?")
            from_date = str(input('Enter date(yyyy-mm-dd hh:mm:ss): '))
            dt = datetime.datetime.strptime(from_date, '%Y-%m-%d %H:%M:%S')
            epoch = dt.timestamp()
            currentTime = (time.time())
            int(currentTime)
            realWhenToRemind = epoch - currentTime
            while True:
                notification.notify(
                    title='REMINDER!!',
                    message=f"{query}",
                    app_icon="C:\\Users\\Asus\\Desktop\\icon.ico",
                    timeout=10
                )
                time.sleep(realWhenToRemind)
        elif "let's play a game" in query:
            speak("challenge accepted")
            board = {1: ' ', 2: ' ', 3: ' ',
                     4: ' ', 5: ' ', 6: ' ',
                     7: ' ', 8: ' ', 9: ' '}


            def printBoard(board):
                print(board[1] + '|' + board[2] + '|' + board[3])
                print('-+-+-')
                print(board[4] + '|' + board[5] + '|' + board[6])
                print('-+-+-')
                print((board[7] + '|' + board[8] + '|' + board[9]))
                print("\n")


            printBoard(board)


            def spaceIsFree(position):
                if (board[position] == ' '):
                    return True
                else:
                    return False


            def insertLetter(letter, position):

                if spaceIsFree(position):
                    board[position] = letter
                    printBoard(board)
                    if (checkDraw()):
                        print('Draw!')
                        exit()
                    if checkForwin():
                        if letter == 'X':
                            print("Bot wins!")
                            exit()
                        else:
                            print("Player wins!")
                            exit()

                    return
                else:
                    print('cant insert there')
                    position = int(input("enter new position: "))
                    insertLetter(letter, position)
                    return


            def checkForwin():
                if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
                    return True
                elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
                    return True
                elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
                    return True
                elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
                    return True
                elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
                    return True
                elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
                    return True
                elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
                    return True
                elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
                    return True
                else:
                    return False


            def checkWhichMarkWon(mark):
                if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
                    return True
                elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
                    return True
                elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
                    return True
                elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
                    return True
                elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
                    return True
                elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
                    return True
                elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
                    return True
                elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
                    return True
                else:
                    return False

            def checkDraw():
                for key in board.keys():
                    if board[key] == ' ':
                        return False
                return True


            player = '0'
            bot = 'X'

            def playerMove():
                position = int(input("Enter the position for '0': "))
                insertLetter(player, position)
                return

            def compMove():
                bestScore = -1000
                bestMove = 0

                for key in board.keys():
                    if (board[key] == ' '):
                        board[key] = bot
                        score = minimax(board, 0, False)
                        board[key] = ' '
                        if (score > bestScore):
                            bestScore = score
                            bestMove = key

                insertLetter(bot, bestMove)

            def minimax(board, depth, isMaximizing):
                if (checkWhichMarkWon(bot)):
                    return 1
                elif (checkWhichMarkWon(player)):
                    return -1
                elif (checkDraw()):
                    return 0

                if (isMaximizing):
                    bestScore = -800
                    for key in board.keys():
                        if (board[key] == ' '):
                            board[key] = bot
                            score = minimax(board, depth + 1, False)
                            board[key] = ' '
                            if (score > bestScore):
                                bestScore = score
                    return bestScore

                else:
                    bestScore = 800
                    for key in board.keys():
                        if (board[key] == ' '):
                            board[key] = player
                            score = minimax(board, depth + 1, True)
                            board[key] = ' '
                            if (score < bestScore):
                                bestScore = score
                    return bestScore


            while not checkForwin():
                compMove()
                playerMove()
        elif "let's play rock paper scissors" in query:
            speak('why not sir')
            while True:
                choices = ["rock", "paper", "scissors"]

                computer = random.choice(choices)
                player = None

                while player not in choices:
                    player = input("rock, paper, or scissors?: ").lower()

                if player == computer:
                    print("computer: ", computer)
                    print("player: ", player)
                    print("Tie!")
                    speak('i guess we are at the same level')

                elif player == "rock":
                    if computer == "paper":
                        print("computer: ", computer)
                        print("player: ", player)
                        print("You lose!")
                        speak('nice try sir')
                    if computer == "scissors":
                        print("computer: ", computer)
                        print("player: ", player)
                        print("You win!")
                        speak('i knew ur the best sir')

                elif player == "scissors":
                    if computer == "rock":
                        print("computer: ", computer)
                        print("player: ", player)
                        print("You lose!")
                        speak('nice try sir')
                    if computer == "paper":
                        print("computer: ", computer)
                        print("player: ", player)
                        print("You win!")
                        speak('i knew ur the best sir')

                elif player == "paper":
                    if computer == "scissors":
                        print("computer: ", computer)
                        print("player: ", player)
                        print("You lose!")
                        speak('nice try sir')
                    if computer == "rock":
                        print("computer: ", computer)
                        print("player: ", player)
                        print("You win!")
                        speak('i knew ur the best sir')

                play_again = input("Play again? (yes/no): ").lower()

                if play_again != "yes":
                    break

            print("Bye!")
            speak('good game sir')
        elif "send sms to mum" in query:
            what_to_send = query.replace('send sms to mum', '')
            speak(f'texting mom, {what_to_send}')
            client = Client(number.account_sid, number.auth_token)
            message = client.messages.create(
                to=number.target_number,
                from_=number.twilio_number,
                body=f"{what_to_send}"
            )

            print(message.body)
            speak(f"message sent to mom {what_to_send}")
        elif "call" in query:
            callWho = query.replace("call", '')
            speak(f'calling, {callWho}')

            def WhatsappCall(name):
                startfile("C:\\ProgramData\\ASUS\\WhatsApp\\WhatsApp.exe")
                sleep(15)
                click(x=50, y=125)
                sleep(1)
                write(name)
                sleep(1)
                click(x=188, y=275)
                sleep(1)
                click(x=571, y=690)
                sleep(1)
                click(x=1750, y=63)


            WhatsappCall(f'{callWho}')
        elif 'message mum' in query:
            message_to_send = query.replace('message mum', '')
            speak(f'messaging mom, {message_to_send}')
            def WhatsappMsg(name, message):
                startfile('C:\\ProgramData\\ASUS\\WhatsApp\\WhatsApp.exe')
                sleep(15)
                click(x=50, y=125)
                sleep(1)
                write(name)
                sleep(1)
                click(x=188, y=275)
                sleep(1)
                click(x=1023, y=745)
                write(message)
                sleep(1)
                click(x=1860, y=1000)
            WhatsappMsg('aaru', f'{message_to_send}')
        elif "play a random song" in query:
            final_song = random.choice(number.favorite_songs)
            speak(f'playing {final_song} from spotify')
            startfile('C:\\Users\\Asus\\AppData\\Roaming\\Spotify\\Spotify.exe')
            sleep(10)
            click(x=50, y=110)
            sleep(1)
            click(x=500, y=50)
            write(f'{final_song}')
            sleep(1)
            click(x=850, y=470)
            sleep(1)
            click(x=850, y=470)
        elif "max volume" in query:
            i = 0
            while i <= 50:
                pyautogui.press("volumeup")
                i = i + 1
        elif "mute" in query:
            pyautogui.press('volumemute')
        elif "increase volume" in query:
            speak("what value should i set as the volume?")
            volume_to_be_set = int(input("what value to set as volume: "))
            volume_to_be_set = volume_to_be_set / 2
            i = 0
            while i <= 50:
                pyautogui.press("volumedown")
                i = i + 1
            i = 1
            while i <= volume_to_be_set:
                pyautogui.press("volumeup")
                i = i + 1
        elif 'alarm' in query:
            alarmH = int(input('what hour do you want the alarm to ring?: '))
            alarmM = int(input('what minute do you want the alarm to ring?: '))
            amPm = str(input('am or pm?: '))
            print("waiting for alarm", alarmH, alarmM, amPm)
            speak(f'alarm is set for {alarmH} hours and {alarmM} minutes on the clock')
            if (amPm == 'pm'):
                alarmH = alarmH + 12
                while True:
                    if alarmH == datetime.datetime.now().hour and alarmM == datetime.datetime.now().minute:
                        print("ALARM!!")

                        notification.notify(
                            title='ALARM!!',
                            message="TIMES UP",
                            app_icon="C:\\Users\\Asus\\Desktop\\icon.ico",
                            timeout=10
                        )
                        playsound('audio.mp3')
                        break
        elif 'tell me a joke' in query:
            the_joke = pyjokes.get_joke()
            print(the_joke)
            speak(the_joke)
        elif 'send mail to sunil' in query:
            email_sender = 'SENDER@gmail.com'
            email_password = number.google_account
            email_reciver = 'RECIEVER@gmail.com'
            query = query.replace('send mail to sunil', '')
            subject = 'mail from SENDER'
            body = f"""
            {query}
            """
            em = EmailMessage()
            em['from'] = email_sender
            em['to'] = email_reciver
            em['Subject'] = subject
            em.set_content(body)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_reciver, em.as_string())
            print('mail sent')
            speak('mail sent')
        elif 'send mail to mum' in query:
            email_sender = 'SENDER@gmail.com'
            email_password = number.google_account
            email_reciver = 'RECIEVER@gmail.com'
            query = query.replace('send mail to mum', '')
            subject = 'mail from SENDER'
            body = f"""
            {query}
            """
            em = EmailMessage()
            em['from'] = email_sender
            em['to'] = email_reciver
            em['Subject'] = subject
            em.set_content(body)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_reciver, em.as_string())
            print('mail sent')
            speak('mail sent')
        elif 'give me directions to' in query:
            speak('have a safe journey sir')
            query = query.replace("give me directions to", '')
            webbrowser.open('https://www.google.co.in/maps')
            time.sleep(10)
            click(x=202, y=94)
            time.sleep(1)
            write(f'{query}')
            sleep(1)
            click(x=373, y=104)
            sleep(2)
            click(x=78, y=264)
        elif 'latest news' in query:
            speak('coming up, top 5 headlines in India today')
            api_key = number.news_api
            def news():
                main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=115de16ee9c0400f8169f07eb28dd451"
                news = yahoo_fin.requests.get(main_url).json()
                articles = news['articles']
                news_articles = []
                for arti in articles:
                    news_articles.append(arti['title'])
                for i in range(5):
                    the_i = f'{i+1})'
                    newz = the_i, news_articles[i]
                    print(newz)
                    speak(newz)
            news()
        elif 'desktop' in query:
            click(x=1919, y=1056)
            speak('now showing desktop')
        elif 'close the window' in query:
            click(x=1832, y=236)
            speak('window is now closed')
        elif 'stock' in query:
            nifty_50_PRICE = round(get_live_price('^NSEI'))
            apple_PRICE = round(get_live_price('AAPL'))
            bse_PRICE = round(get_live_price('^BSESN'))
            hdfc_PRICE = round(get_live_price('HDFCBANK.NS'))
            reliance_PRICE = round(get_live_price('RELIANCE.NS'))
            print("1) nifty 50:", nifty_50_PRICE)
            print("2) apple:", apple_PRICE)
            print("3) BSE:", bse_PRICE)
            print("4) HDFC:", hdfc_PRICE)
            print("5) reliance:",reliance_PRICE)
            speak(f'number 1, nifty fifty is now at: {nifty_50_PRICE} rupees'
                  f'number 2, apple is now at: {apple_PRICE} rupees'
                  f'number 3, BSE is now at: {bse_PRICE} rupees'
                  f'number 4, hdfc bank is now at {hdfc_PRICE } rupees'
                  f'number 5, reliance is now at {reliance_PRICE} rupees')
        elif 'add to my to do list' in query:
            query = query.replace("add to my to do list", '')
            click(x=1038, y=1063)
            sleep(7)
            click(x=395, y=968)
            sleep(1)
            write(f'{query}')
            sleep(1)
            pyautogui.press('enter')
            sleep(1)
            click(x=1897, y=11)
            speak(f'reminder set, {query}')
        elif 'add to my to-do list' in query:
            query = query.replace("add to my to-do list", '')
            click(x=1038, y=1063)
            sleep(7)
            click(x=395, y=968)
            sleep(1)
            write(f'{query}')
            sleep(1)
            pyautogui.press('enter')
            sleep(1)
            click(x=1897, y=11)
            speak(f'reminder set, {query}')
        elif 'show me my tasks for the day' in query:
            click(x=1090, y=1060)
            sleep(2)
            speak('these are the tasks left to do today')
        elif 'translate this into hindi' in query:
            query = query.replace('translate this into hindi', '')
            webbrowser.open('https://translate.google.com/')
            sleep(5)
            click(x=1277, y=255)
            sleep(1)
            click(x=379, y=285)
            sleep(1)
            write('hindi')
            sleep(1)
            click(x=377, y=364)
            sleep(1)
            click(x=346, y=315)
            write(f'{query}')
            sleep(3)
            click(x=986, y=410)
        elif 'sports news' in query:
            client = gnewsclient.NewsClient(language='english', location='india',topic='sports',max_results=5)
            newsList = client.get_news()
            speak('the top 5 sports news for today are: ')
            for item in newsList:
                titles_sports_news = item['title']
                sports_news_links = item['link']
                print("")
                print("Tittle --", titles_sports_news)
                print("Link -- ", sports_news_links)
            for item in newsList:
                titles_sports_news_speak = item['title']
                speak(titles_sports_news_speak)
        elif 'world news' in query:
            client = gnewsclient.NewsClient(language='english', location='india', topic='world', max_results=5)
            newsList = client.get_news()
            speak('the top 5 news in the world for today are: ')
            for item in newsList:
                titles_world_news = item['title']
                world_news_links = item['link']
                print("")
                print("Tittle --", titles_world_news)
                print("Link -- ", world_news_links)
            for item in newsList:
                titles_world_news_speak = item['title']
                speak(titles_world_news_speak)
        elif 'tech news' in query:
            client = gnewsclient.NewsClient(language='english', location='india', topic='Technology', max_results=5)
            newsList = client.get_news()
            speak('the top 5 tech news for today are: ')
            for item in newsList:
                titles_tech_news = item['title']
                tech_news_links = item['link']
                print("")
                print("Tittle --", titles_tech_news)
                print("Link -- ", tech_news_links)
            for item in newsList:
                titles_world_news_speak = item['title']
                speak(titles_world_news_speak)
        elif 'recipe of' in query:
            query = query.replace('recipe of', '')
            webbrowser.open(f'https://www.allrecipes.com/search/results/?search={query}')
            sleep(2)
            speak(f'here are some recipes for {query}')
        elif 'open hotstar and play' in query:
            query = query.replace("open hotstar and play", '')
            webbrowser.open('https://www.hotstar.com/in')
            sleep(15)
            click(x=1692, y=143)
            sleep(3)
            write('iron man 2')
            sleep(3)
            click(x=1526, y=203)
            sleep(3)
            click(x=113, y=660)
        elif 'network speed' in query:
            wifi = speedtest.Speedtest()
            speed = round(wifi.download() / (10 ** 6), 3)
            print(f"the network speed is {speed} mega bits per second")
            speak(f"the network speed is {speed} mega bits per second")
        else:
            openai.api_key = "API_KEY"
            model_engine = "text-davinci-003"
            prompt = f"{query}"

            completion = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            response = completion.choices[0].text
            print(response)
            speak(response)

