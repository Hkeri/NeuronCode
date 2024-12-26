import webbrowser
from time import sleep
import pyautogui
from re import search
from keyboard import press_and_release
import os
from datetime import datetime
from features.speak import speak
from psutil import sensors_battery, net_io_counters
from screen_brightness_control import set_brightness
from django.core.mail import send_mail
import ctypes
import os
import psutil
import tempfile
import os
import requests
import speech_recognition as sr
import shutil
from pypdf import PdfReader
from notifypy import Notify
import easyocr

def ocr(image_path):
    # Initialize the EasyOCR reader
    reader = easyocr.Reader(['en'])  # Specify the language(s) you want to use

    # Path to the image file
    image_path = image_path  # Replace with your image path

    # Perform OCR on the image
    results = reader.readtext(image_path)

    # Print the detected text
    for (bbox, text, prob) in results:
        return (text)

def playMusic(song_name):
    try:
        import pywhatkit
        pywhatkit.playonyt(song_name)
        speak(f"Playing {song_name}")
    except Exception as e:
        speak("Sir I cannot play that certain song")

def notify(text):
    notification = Notify
    notification.title = "Neuron"
    notification.message = text
    notification.send()
    
def read_pdf(pdf_file):
    # creating a pdf reader object
    reader = PdfReader(pdf_file)

    # printing number of pages in pdf file
    print(len(reader.pages))

    # getting a specific page from the pdf file
    page = reader.pages[0]

    # extracting text from page
    text = page.extract_text()
    return text

def organize_files(directory):
    os.chdir(directory)

    for filename in os.listdir(directory):
        if os.path.isdir(filename):
            continue
        
        file_extension = filename.split('.')[-1] if '.' in filename else 'no_extension'
        
        # Create specific folders for Word and Excel files
        if file_extension in ['doc', 'docx']:
            target_folder = 'Word'
        elif file_extension in ['xls', 'xlsx']:
            target_folder = 'Excel'
        elif file_extension in ['pptx']:
            target_folder = 'PowerPoint'
        elif file_extension in ['pdf']:
            target_folder = 'PDF'
        elif target_folder in ['exe']:
            target_folder = 'Applications'
        elif file_extension in ['py', 'java', 'html', 'css', 'js']:
            target_folder = 'Code'
        else:
            target_folder = file_extension
        
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        
        shutil.move(filename, os.path.join(target_folder, filename))
        print(f'Moved: {filename} to {target_folder}/')

def file_organizer(directory):
    if os.path.isdir(directory):
        organize_files(directory)
        return ("Files organized successfully.")
    else:
        return ("The specified directory does not exist.")

def transcribe_audio(file_path):
    # Create a speech recognition object
    r = sr.Recognizer()

    # Open the audio file
    with sr.AudioFile(file_path) as source:
        # Read the audio data
        audio = r.record(source)

        # Transcribe the audio
        try:
            transcription = r.recognize_google(audio)
            return transcription
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError:
            return "Could not request results"

def download_images(image_urls):
    for url in image_urls:
        response = requests.get(url)
        if response.status_code == 200:
            image_name = url.split("/")[-1]
            with open(image_name, 'wb') as img_file:
                img_file.write(response.content)
            return (f"Downloaded: {image_name}")
        else:
             return (f"Failed to download {url}: {response.status_code}")

def clean_temp():
    temp_dir = tempfile.gettempdir()
    for filename in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, filename)
        try:
            os.remove(file_path)
        except Exception as e:
            return (f"Error deleting file {file_path}: {e}")

def get_file_extension(text):

    if "python file" in text:
        ex = ".py"
    elif "java file" in text:
        ex = ".java"
    elif "text file" in text:
        ex = ".txt"
    elif "html file" in text:
        ex = ".html"
    elif "css file" in text:
        ex = ".css"
    elif "javascript file" in text:
        ex = ".js"
    elif "json file" in text:
        ex = ".json"
    elif "xml file" in text:
        ex = ".xml"
    elif "csv file" in text:
        ex = ".csv"
    elif "markdown file" in text:
        ex = ".md"
    elif "yaml file" in text:
        ex = ".yaml"
    elif "pdf file" in text:
        ex = ".pdf"
    elif "word file" in text:
        ex = ".docx"
    elif "excel file" in text:
        ex = ".xlsx"
    elif "powerpoint file" in text:
        ex = ".pptx"
    elif "zip file" in text:
        ex = ".zip"
    elif "tar file" in text:
        ex = ".tar"
    else:
        ex = ""  # Default case if no match found
    return ex

def update_text(text):
    if "python file" in text:
        text = text.replace("python file", "")
    elif "java file" in text:
        text = text.replace("java file", "")
    elif "text file" in text:
        text = text.replace("text file", "")
    elif "html file" in text:
        text = text.replace("html file", "")
    elif "css file" in text:
        text = text.replace("css file", "")
    elif "javascript file" in text:
        text = text.replace("javascript file", "")
    elif "json file" in text:
        text = text.replace("json file", "")
    elif "xml file" in text:
        text = text.replace("xml file", "")
    elif "csv file" in text:
        text = text.replace("csv file", "")
    elif "markdown file" in text:
        text = text.replace("markdown file", "")
    elif "yaml file" in text:
        text = text.replace("yaml file", "")
    elif "image file" in text:
        text = text.replace("image file", "")
    elif "video file" in text:
        text = text.replace("video file", "")
    elif "audio file" in text:
        text = text.replace("audio file", "")
    elif "pdf file" in text:
        text = text.replace("pdf file", "")
    elif "word file" in text:
        text = text.replace("word file", "")
    elif "excel file" in text:
        text = text.replace("excel file", "")
    elif "powerpoint file" in text:
        text = text.replace("powerpoint file", "")
    elif "zip file" in text:
        text = text.replace("zip file", "")
    elif "tar file" in text:
        text = text.replace("tar file", "")
    else:
        pass
    return text



def create_file(text):
    selected_ex = get_file_extension(text)
    text = update_text(text)
    if "named" in text or "with name" in text:
        text = text.replace("named","")
        text = text.replace("with name","")
        text = text.replace("create","")
        text = text.strip()
        with open(f"{text}{selected_ex}","w"):
            pass
    else :
        with open(f"demo{selected_ex}","w"):
            pass

def get_top_processes(num_processes=3):
    # Create a list to hold process information
    processes = []

    # Iterate through all running processes
    for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
        try:
            # Get CPU and memory usage
            cpu_usage = process.info['cpu_percent']
            memory_usage = process.info['memory_info'].rss  # Resident Set Size (RSS)

            # Append process info to the list
            processes.append((process.info['name'], cpu_usage, memory_usage))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            # Handle the case where the process has terminated or access is denied
            continue

    # Sort processes by CPU usage and then by memory usage
    processes.sort(key=lambda p: (p[1], p[2]), reverse=True)

    # Get the top 'num_processes' processes
    top_processes = processes[:num_processes]

    return top_processes

def display_top_processes():
    top_processes = get_top_processes()
    for name, cpu, memory in top_processes:
        return (f"Process: {name}, CPU Usage: {int(cpu)}, Memory Usage: {int(memory / (1024 * 1024))}")  # Convert bytes to MB
    

def change_wallpaper(image_path):
    # Check if the file exists
    if not os.path.isfile(image_path):
        print(f"The file {image_path} does not exist.")
        print("You Can Go back to The main Menu")

    # Use the SystemParametersInfo function from user32.dll
    try:
        # SPI_SETDESKWALLPAPER = 20
        # SPIF_UPDATEINIFILE = 0x01
        # SPIF_SENDCHANGE = 0x02
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        print("Wallpaper changed successfully.")
    except Exception as e:
        print(f"Failed to change wallpaper: {e}")


def send_email(message, email):
    send_mail(
        "",
        message,
        email,
        fail_silently=False,
    )

def dim_light():
    set_brightness(45)

def wishme():
    speak("Hello There Sir.")
    speak("And Also")
    events()
    speak(
        f"The Time is {datetime.now().hour} hours and {datetime.now().minute} minutes"
    )
    speak(
        "I am Jarvis, Your Personal Assistant, How would you like to Start our Day?"
    )

def internet_speed():
        # Select network interface (replace 'en0' with your interface)
        net_if = net_io_counters(pernic=True)['en0']

        # Initial byte counts
        bytes_recv = net_if.bytes_recv

        sleep(3)  # Measure for 3 seconds

        # Calculate bytes transferred
        new_bytes_recv = net_if.bytes_recv
        recv = new_bytes_recv - bytes_recv

        # Convert to Mbps
        download_speed = recv / (5 * 1024 * 1024)

        return f"Internet Speed: {download_speed:.2f} Mbps"

def smart_battery():
    batt = sensors_battery()
    if batt.power_plugged:
        speak(f"The Battery is Currently {batt.percent}")

    else:
        if batt.percent <= 75:
            speak(
                f"The Battery is {batt.percent} and it is Perfect!"
            )

        elif batt.percent <= 50 and batt.percent >= 75:
            speak(
                f"The Battery is {batt.percent} and it is at good charge!"
            )

        elif batt.percent <= 25 and batt.percent >= 50:
            speak(
                f"The Battery is {batt.percent} but you \nhave to charge since it is kinda low!"
            )

        elif batt.percent <= 10 and batt.percent >= 25:
            speak(
                f"The Battery is {batt.percent} so really you must charge it right away!"
            )

        elif batt.percent <= 5 and batt.percent >= 10:
            speak(
                f"Sir, You must charge you computer right now because it is {batt.percent}"
            )

        else:
            speak(
                f"Sir it is Extremely Low because it is {batt.percent}. \nCharge it Immediately!"
            )


def yt_search(user):
    user = user.replace("youtube search", "")
    user = user.replace("Youtube search", "")
    user = user.replace("youtube Search", "")
    webbrowser.open(f"https://www.youtube.com/results?search_query={user}")
    return (
        "Sir! This is what I found on Youtube According to Your user!"
    )

def events():
        if datetime.now().strftime("%m") == "12":
            if datetime.now().strftime("%d") == "25":
                speak("Merry Christmas Sir")
        else:
            pass

        if datetime.now().strftime("%m") == "06":
            if datetime.now().strftime("%d") == "21":
                speak("Happy Father's Day to Your Father Sir")
        else:
            pass

        if datetime.now().strftime("%m") == "05":
            if datetime.now().strftime("%d") == "08":
                speak(
                    "Happy Internation Mother's Day to Your Mother Sir"
                )
        else:
            pass

        if datetime.now().strftime("%m") == "05":
            if datetime.now().strftime("%d") == "17":
                speak("Happy Saint Patrick's Day Sir")
        else:
            pass

        if datetime.now().strftime("%m") == "01":
            if datetime.now().strftime("%d") == "01":
                speak("Happy New Year Sir")
        else:
            pass

        if datetime.now().strftime("%m") == "10":
            if datetime.now().strftime("%d") == "31":
                speak("Happy Halloween Sir")
        else:
            pass

        if datetime.now().strftime("%m") == "04":
            if datetime.now().strftime("%d") == "01":
                speak("Happy April Fool's Sir")
        else:
            pass

        if datetime.now().strftime("%m") == "11":
            if datetime.now().strftime("%d") == "28":
                speak("Happy Thanksgiving Sir")
        else:
            pass

def openappweb(query):
    if search(".com" or ".co" or ".org", query):
        query = query.replace("open", "")
        query = query.replace("jarvis", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    else:
        file_to_open = query.lower()
        file_to_open = query.replace("open ", "")
        file_to_open = file_to_open.replace("launch", "")
        file_to_open = file_to_open.replace("command prompt", "cmd")
        file_to_open = file_to_open.replace("word", "winword")
        file_to_open = file_to_open.replace("vscode", "code")
        file_to_open = file_to_open.replace("visual studio code", "code")
        file_to_open = file_to_open.replace("power point", "powerpnt")
        file_to_open = file_to_open.replace("excel", "excel")
        file_to_open = file_to_open.replace("google chrome", "chrome")
        file_to_open = file_to_open.replace("firefox", "firefox")
        file_to_open = file_to_open.replace("edge", "msedge")
        file_to_open = file_to_open.replace("notepad", "notepad")
        file_to_open = file_to_open.replace("calculator", "calc")
        file_to_open = file_to_open.replace("spotify", "spotify")
        file_to_open = file_to_open.replace("discord", "discord")
        file_to_open = file_to_open.replace("zoom", "zoom")
        file_to_open = file_to_open.replace("teams", "teams")
        file_to_open = file_to_open.replace("outlook", "outlook")
        file_to_open = file_to_open.replace("powershell", "powershell")
        file_to_open = file_to_open.replace("adobe reader", "acrord32")
        file_to_open = file_to_open.replace("vlc media player", "vlc")
        press_and_release("win + r")
        sleep(0.5)
        pyautogui.typewrite(f"{file_to_open.lower()}.exe")
        sleep(0.5)
        press_and_release("enter")

def closeappweb(query):
    if search("tab", query):
        pyautogui.hotkey("ctrl", "w")
    else:
        file_to_close = query.lower()
        file_to_close = query.replace("jarvis", "")
        file_to_close = query.replace("close ", "")
        file_to_close = file_to_close.replace("launch", "")
        file_to_close = file_to_close.replace("command prompt", "cmd")
        file_to_close = file_to_close.replace("word", "winword")
        file_to_close = file_to_close.replace("vscode", "code")
        file_to_close = file_to_close.replace("visual studio code", "code")
        file_to_close = file_to_close.replace("power point", "powerpnt")
        file_to_close = file_to_close.replace("excel", "excel")
        file_to_close = file_to_close.replace("google chrome", "chrome")
        file_to_close = file_to_close.replace("firefox", "firefox")
        file_to_close = file_to_close.replace("edge", "msedge")
        file_to_close = file_to_close.replace("notepad", "notepad")
        file_to_close = file_to_close.replace("calculator", "calc")
        file_to_close = file_to_close.replace("spotify", "spotify")
        file_to_close = file_to_close.replace("discord", "discord")
        file_to_close = file_to_close.replace("zoom", "zoom")
        file_to_close = file_to_close.replace("teams", "teams")
        file_to_close = file_to_close.replace("outlook", "outlook")
        file_to_close = file_to_close.replace("powershell", "powershell")
        file_to_close = file_to_close.replace("adobe reader", "acrord32")
        file_to_close = file_to_close.replace("vlc media player", "vlc")
        os.system(f"taskkill /f /im {file_to_close}.exe")