from PIL import Image, ImageTk
import requests
from datetime import datetime
import sys
python_exe_location = str(sys.executable)
open_weather_app_id = "57750a40690b5a50f53cc755c386cfbc"
dir_agi = "\\Neuron_App"
import customtkinter
from LLM.processor import response, image_generation
import random
from features.speak import speak
import pywhatkit
from pwinput import pwinput
import psutil
from pytube import YouTube
import webbrowser
import platform
import warnings
from functools import lru_cache
from features.basic import (
    dim_light,
    openappweb,
    closeappweb,
    change_wallpaper,
    send_email,
    display_top_processes,
    create_file,
    clean_temp,
    download_images,
    transcribe_audio,
    file_organizer,
    playMusic,
    ocr
)
import time
import qrcode
import keyboard
import os
import re
from features import age_safety
import subprocess
import pyautogui
from features import melody_generator
import cv2


def destroy():
    customtkinter.CTk().after(2000, root.destroy())


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme(f"{dir_agi}\\images\\cyan.json")
warnings.filterwarnings("ignore")
root = customtkinter.CTk()
customtkinter.set_widget_scaling(0.80)
customtkinter.set_window_scaling(1)
root.attributes('-alpha', 0.935)
root.resizable(False, False)


def is_cam_opened():
    cap = cv2.VideoCapture(0)

    if cap.isOpened():
        cap.release()
        print("Camera is Available")

    if not cap.isOpened():
        print("Camera is Not Available")


root.iconbitmap(f"{dir_agi}\\images\\agi_icon_2.ico")
mode = "dark"
dark_sync = [
    "reg.exe",
    "add",
    "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize",
    "/v",
    "AppsUseLightTheme",
    "/t",
    "REG_DWORD",
    "/d",
    "0",
    "/f",
]

light_sync = [
    "reg.exe",
    "add",
    "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize",
    "/v",
    "AppsUseLightTheme",
    "/t",
    "REG_DWORD",
    "/d",
    "1",
    "/f",
]

subprocess.call(dark_sync)
root.title("NEURON")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
x = (width / 2) - (1066 / 2)
y = (height / 2) - (518 / 2)
root.geometry(f"1066x518+{int(x)}+{int(y)}")
my_font = customtkinter.CTkFont(family="Consolas", size=25, slant="italic")
my_font_for_buttons = customtkinter.CTkFont(family="Consolas", size=15)
my_font_for_buttons_2 = customtkinter.CTkFont(family="Consolas", size=13)


@lru_cache
def Temp(city):
    import json

    api_key = (
        open_weather_app_id
    )  # Replace with your actual OpenWeatherMap API key
    endpoint = "http://api.openweathermap.org/data/2.5/weather"

    # send GET request to API endpoint
    response = requests.get(
        endpoint, params={"q": city, "appid": api_key, "units": "metric"}
    )

    # check if the request was successful
    if response.status_code == 200:
        # parse JSON response
        data = json.loads(response.text)

        # check if 'main' key is present
        if "main" in data:
            # extract temperature in Celsius
            temperature_celsius = data["main"]["temp"]
            return temperature_celsius
        else:
            add("Error: 'main' key not found in API response")
    else:
        add(
            f"Error: Failed to fetch data from API. \nStatus code: {
                response.status_code}")
    IP = requests.get("https://api.ipify.org").text
    url = "https://get.geojs.io/v1/ip/geo/" + IP + ".json"
    geo_reqeust = requests.get(url)
    geo_data = geo_reqeust.json()
    city = geo_data["city"]

    city = city
    return None


def change():
    global mode
    if mode == "dark":
        customtkinter.set_appearance_mode("light")
        subprocess.run(light_sync)
        mode = "light"

    else:
        customtkinter.set_appearance_mode("dark")
        subprocess.run(dark_sync)
        mode = "dark"


quotes = [
    '"Love what you do."',
    '"Believe in yourself."',
    '"Create your own future."',
    '"Never give up."',
    '"Doubt limits your tomorrow."',
    '"Fear is the enemy."',
    '"See opportunity in challenges."',
    '"Work hard, get lucky."',
    '"Happiness leads to success."',
    '"Find yourself by serving others."',
    '"Rise after every fall."',
    '"Success comes from hard work."',
    '"Your beliefs limit your goals."',
    '"Start doing, stop talking."',
    '"Dream big, achieve big."',
    '"Do something for your future self."',
    '"Find light in darkness."',
    '"Learn from failures."',
    '"Dream without limits."',
    '"Take calculated risks."',
    '"Start small, dream big."',
    '"Keep moving forward."',
    '"Effort equals reward."',
    '"Dream big, do bigger."',
    '"Build your own destiny."',
    '"Live your dreams."',
    '"Beauty comes from within."',
    '"Success is the best revenge."',
    '"Actions speak louder than words."',
    '"Creativity is endless."',
    '"Learn from mistakes."',
    '"Do the impossible."',
    '"Focus on the process."',
    '"Try new things."',
    '"Defeat is temporary."',
    '"Start now, win later."',
    '"Age is just a number."',
    '"Opportunity is everywhere."',
    '"Your mind is your limit."',
    '"Live your own life."',
    '"Great work brings satisfaction."',
    '"Embrace challenges."',
    '"Age is no barrier to success."',
]


def qrCodeGenerator(input_Text_link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )
    QRfile_name = (str(datetime.now().strftime("%d-%m-%Y"))).replace(" ", "-")
    QRfile_name = QRfile_name.replace(":", "-")
    QRfile_name = QRfile_name.replace(".", "-")
    QRfile_name = QRfile_name + "-QrCode.png"
    qr.add_data(input_Text_link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{QRfile_name}")
    os.startfile(f"{os.getcwd()}\\{QRfile_name}")


def ytDownloader(yt_url):
    yt = YouTube(yt_url)
    video = yt.streams.get_highest_resolution()
    video.download()


def whatsapp_send():
    global button2_pressed

    def delete():
        input_box.delete(0, "end")

    add("Please Type in The Details")
    time.sleep(4.5)
    delete()
    add("Contact or Group ->")

    # Get the mode from the input box
    mode = input_box.get().lower()

    if mode == "contact":
        try:
            delete()
            add("Phone Number (country code as well with +): ")
            if button2_pressed:  # Check if button2 is pressed
                phone_number = input_box.get()
                delete()
                add(f"What Text Do You Want To Send to {phone_number}: ")
                if button2_pressed:  # Check if button2 is pressed
                    message = input_box.get()

                    time_hour = 14
                    time_minute = 50
                    waiting_time_to_send = 15
                    close_tab = True
                    waiting_time_to_close = 2

                    pywhatkit.sendwhatmsg(
                        phone_number,
                        message,
                        time_hour,
                        time_minute,
                        waiting_time_to_send,
                        close_tab,
                        waiting_time_to_close,
                    )
                    add("I Have Sent Your Message")
        except Exception as e:
            add(f"Message Could Not be Sent to {phone_number}: {str(e)}")

    elif mode == "group":
        try:
            delete()
            add("Group ID: ")
            if button2_pressed:  # Check if button2 is pressed
                group_id = input_box.get()
                delete()
                add("What Text Do You Want To Send To The Group: ")
                if button2_pressed:  # Check if button2 is pressed
                    message = input_box.get()

                    time_hour = 14
                    time_minute = 50
                    waiting_time_to_send = 15
                    close_tab = True
                    waiting_time_to_close = 2

                    pywhatkit.sendwhatmsg_to_group(
                        group_id,
                        message,
                        time_hour,
                        time_minute,
                        waiting_time_to_send,
                        close_tab,
                        waiting_time_to_close,
                    )
                    add("I Have Sent Your Message to the Group")
        except Exception as e:
            add(f"Message Could Not be Sent to The Group: {str(e)}")

    else:
        add("Please Type in The Following Options: 'Contact' or 'Group'")
        whatsapp_send()


def output():
    global button2_pressed
    user = input_box.get().lower()

    def delete():
        input_box.delete(0, "end")

    if re.search(
            ("reduce" or "dim" or "lower") and (
                "light" or "lights" or "brightness"),
            user):
        dim_light()
        add("I have Dimmed The Brightness")

    if re.search("increase" and "volume", user):
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        add("I have increased the Volume")

    if re.search("decrease" and "volume", user):
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        add("I have decreased the Volume")

    if re.search("mute" and ("the volume" or "volume"), user):
        pyautogui.press("volumemute")

    if re.search("unmute" and ("the volume" or "volume"), user):
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

    if re.search("screenshot", user):
        number = 0
        speak("Sure Sir, I will give you 5 seconds to show you want to Screenshot")
        time.sleep(5)
        ss = pyautogui.screenshot()
        number += 1
        ss.save(f"screenshot_{number}.png")
        add("I Have made A screenshot sir")

    if re.search("shutdown", user):
        if platform.system() == "Windows":
            os.system("shutdown /s /t 0")
        elif platform.system() == "Linux":
            os.system("shutdown now")
        elif platform.system() == "Darwin":  # macOS
            os.system("sudo shutdown -h now")

    if re.search("restart", user):
        if platform.system() == "Windows":
            os.system("shutdown /r /t 0")
        elif platform.system() == "Linux":
            os.system("reboot")
        elif platform.system() == "Darwin":  # macOS
            os.system("sudo shutdown -r now")

    if re.search("youtube search", user):
        user = user.replace("youtube search", "")
        user = user.replace("Youtube search", "")
        user = user.replace("youtube Search", "")
        add("Sir! This is what I found on Youtube According to Your user!")
        webbrowser.open(f"https://www.youtube.com/results?search_query={user}")

    if re.search("internet speed", user):
        net_if = psutil.net_io_counters(pernic=True)["en0"]
        # Initial byte counts
        bytes_recv = net_if.bytes_recv
        time.sleep(2.5)  # Measure for 3 seconds
        # Calculate bytes transferred
        new_bytes_recv = net_if.bytes_recv
        recv = new_bytes_recv - bytes_recv
        # Convert to Mbps
        download_speed = recv / (5 * 1024 * 1024)
        add(f"Your Current Download Speed is {download_speed:.2f}")

    if re.search("battery", user):
        batt = psutil.sensors_battery()
        if batt.power_plugged:
            add(f"The Battery is Currently {batt.percent}")

        else:
            if batt.percent <= 75:
                add(f"The Battery is {batt.percent} and it is Perfect!")

            elif batt.percent <= 50 and batt.percent >= 75:
                add(f"The Battery is {batt.percent} and it is at good charge!")

            elif batt.percent <= 25 and batt.percent >= 50:
                add(
                    f"The Battery is {
                        batt.percent} but you \nhave to charge since it is kinda low!")

            elif batt.percent <= 10 and batt.percent >= 25:
                add(
                    f"The Battery is {
                        batt.percent} so really you must charge it right away!")

            elif batt.percent <= 5 and batt.percent >= 10:
                add(
                    f"Sir, You must charge you computer right now because it is {
                        batt.percent}")

            elif batt.percent <= 1 and batt.percent >= 5:
                add(
                    f"Sir it is Extremely Low because it is {
                        batt.percent}. \nCharge it Immediately!")

    if re.search("open", user):
        if re.search("article" or "report" or "research", user):
            topic = response(f"What is the Topic of this Question. '{user}'")
            webbrowser.open(f"https://www.google.com/search?q={topic}")

        if re.search("globe" or "earth", user):
            add("Showing A Globe of Earth")
            earth()

        if re.search("tic tac toe" or "tictactoe" or "tic-tac-toe", user):
            add("Opening Tic Tac Toe Game")
            tictactoe()

        if re.search("task" and "manager", user):
            keyboard.press_and_release("ctrl + shift + escape")
            add("I Have Opened Task Manager")

        if re.search("iss", user):
            add("Opening the ISS GUI")
            iss()

        if re.search("calculator", user):
            calculator()

        if re.search("chess", user):
            chess()

        if re.search("computer" and "status", user):
            add("Showing Computer's Features")
            status()

        else:
            query = user.replace("open ", "")
            query = query.replace("open", "")
            try:
                openappweb(user)
                add(f"I Have Opened {query}")
            except BaseException:
                add(f"I Cannot Open {query}")

    if re.search("close", user):
        query = user.replace("close ", "")
        query = query.replace("close", "")
        try:
            closeappweb(user)
            add(f"I Have Closed {query}")
        except BaseException:
            add(f"I Cannot Close {query}")

    if re.search("whatsapp" and "send", user):
        whatsapp_send()

    if re.search("email" and "send", user):
        def delete():
            input_box.delete(0, "end")
        add("Please Type In The Details")
        time.sleep(4.5)
        delete()
        add("Enter The Email You Want To Send")
        if button2_pressed:
            u_email = input_box.get()
            delete()
            add("Enter The Message You Want to Send")
            if button2_pressed:
                u_message = input_box.get()
        send_email(email=u_email, message=u_message)
        delete()
        add("Email Sended!")

    if re.search(
            ("generate" or "create" or "make") and (
                "melody" or "music" or "song"),
            user):
        melody_generator.main()

    if re.search("change" and "wallpaper", user):
        add("Type the Image Path (Make Sure You Type The Proper path)")
        if button2_pressed:
            image_path = input_box.get()
        change_wallpaper(image_path)

    if re.search("list" and ("processes" or "procesess"), user):
        add(display_top_processes())

    if re.search(("create" or "generate" or "make") and "file", user):
        create_file(user)
        add("File Created!")

    if re.search(
            ("clean" or "destory") and (
                "temp" or "temporary") and (
                "files" or "file"),
            user):
        clean_temp()
        add("Completed Cleaning Temporary Files!")

    if re.search(("download" or "install") and "image", user):
        add("Sure, Please Type in the URL")
        if button2_pressed:
            _url = input_box.get()
        add(download_images(_url))

    if re.search("transcribe" and "audio", user):
        add("Sure Sir, Please Type in the File Path")
        if button2_pressed:
            path_ = input_box.get()
        delete()
        add(transcribe_audio(file_path=path_))

    if re.search("download" and "youtube" and "video", user):
        add("Okay, Type in The Youtube URL")
        if button2_pressed:
            url = input_box.get()
        ytDownloader(url)

    if re.search(("make" or "create") and "qrcode", user):
        add("Okay, Type in The URL for the Qr Code")
        if button2_pressed:
            qr_url = input_box.get()
        qrCodeGenerator(qr_url)

    if re.search(
            ("make" or "create") and (
                "melody" or "music" or "song"),
            user):
        add("Making a Melody")
        melody_generator()

    if re.search("generate" and "image", user):
        add("Okay, Generating an image")
        image_generation(user)
        delete()
        add("Generated the Image!")

    if re.search("organize" and "files", user):
        add("Okay Sir, I will Organize The Files, Can you type in the Directory?")
        if button2_pressed:
            directory_path = input_box.get()
            add(file_organizer(directory_path))

    if re.search("type", user):
        add("Okay, I Will Type it On Your Screen")
        answer = user.replace("type", "make")
        answer = response(answer)
        pyautogui.write(answer)

    if re.search("play", user):
        query = user.replace("play", "")
        query = query.replace("neuron", "")
        playMusic(query)

    if re.search("new" and "meeting", user):
        webbrowser.open("https://meet.new")

    if re.search("read" and "image", user):
        add("Sure Sir, Just type in the Image Path")
        if button2_pressed:
            add(ocr(input_box.get()))

    if (
        not ("organize" and "files")
        or ("generate" and "image")
        or (("download" or "install") and "image")
        or (("clean" or "destory") and ("temp" or "temporary") and ("files" or "file"))
        or (("create" or "generate" or "make") and "file")
        or ("list" and ("processes" or "procesess"))
        or ("change" and "wallpaper")
        or ("generate" and ("melody" or "music" or "song"))
        or ("email" and "")
        or ("whatsapp" and "send")
        or ("close")
        or ("open")
        or ("battery")
        or ("internet speed")
        or ("dim" and ("light" or "lights" or "brightness"))
        or ("increase" and "volume")
        or ("decrease" and "volume")
        or ("mute" and ("the volume" or "volume"))
        or ("unmute" and ("the volume" or "volume"))
        or ("screenshot")
        or ("shutdown")
        or ("restart")
        or ("youtube search")
        or ("transcribe" and "audio")
        or ("download" and "youtube" and "video")
        or (("make" or "create") and "qrcode")
        or ("type")
        or ("new" and "meeting") in user
    ):
        ans = response(user)
        add(ans)


def icon_close():
    customtkinter.set_appearance_mode("dark")
    root.withdraw()
    icon_window = customtkinter.CTkToplevel()
    icon_window.title("Neuron App")
    icon_window.geometry("400x250")

    label_image1 = customtkinter.CTkLabel(
        icon_window, text="Neuron", font=("Consolas", 65))
    label_image1.pack(pady=20)

    def show_original():
        icon_window.destroy()
        customtkinter.set_appearance_mode(mode)
        root.deiconify()

    def destoryicon():
        exit()

    my_button = customtkinter.CTkButton(
        icon_window,
        text="Show Features",
        command=show_original,
        corner_radius=50,
        border_color="#41FDFE")
    my_button.pack(pady=20)
    my_button.place(x=50, y=200)
    my_button2 = customtkinter.CTkButton(
        icon_window,
        text="Exit",
        command=destoryicon,
        corner_radius=50,
        border_color="#41FDFE")
    my_button2.pack(pady=20)
    my_button2.place(x=205, y=200)


def qrcode_gui():
    customtkinter.set_appearance_mode("dark")
    root.withdraw()
    qr_gui = customtkinter.CTkToplevel()
    qr_gui.title("Neuron | QrCode Generator")
    qr_gui.geometry("550x250")

    def show_original():
        qr_gui.destroy()
        customtkinter.set_appearance_mode(mode)
        root.deiconify()

    def destoryicon():
        exit()

    def get_info():
        info = des_entry.get()
        qrCodeGenerator(info)

    des_entry = customtkinter.CTkEntry(
        qr_gui,
        placeholder_text="Enter Text or Link to Put in Your QrCode",
        width=540,
        height=75,
        corner_radius=50,
        font=("Consolas", 18),
    )
    des_entry.pack(pady=20)

    my_button = customtkinter.CTkButton(
        qr_gui,
        text="Show Main",
        command=show_original,
        corner_radius=50,
        font=my_font_for_buttons,
        border_color="#41FDFE"
    )
    my_button.pack(pady=20)
    my_button.place(x=50, y=200)

    enter_button = customtkinter.CTkButton(
        qr_gui,
        text="Done",
        command=get_info,
        corner_radius=50,
        font=my_font_for_buttons,
        border_color="#41FDFE"
    )

    enter_button.pack(pady=20)

    my_button2 = customtkinter.CTkButton(
        qr_gui,
        text="Exit",
        command=destoryicon,
        corner_radius=50,
        font=my_font_for_buttons,
        border_color="#41FDFE"
    )
    my_button2.pack(pady=20)
    my_button2.place(x=450, y=200)


def add(user_text: str):
    os.system("cls" if os.name == "nt" else "clear")
    queries_widget.delete("1.0", "end")
    n = 0

    def animate_label():
        input_box.delete(0, "end")
        nonlocal n
        if n < len(user_text):
            queries_widget.insert("end", user_text[: n + 1])
            root.after(70, animate_label)
            n += 1

    if len(user_text) >= 150:
        root.after(1000, animate_label)
    if len(user_text) <= 150:
        if re.search("yes", is_speaker_working.lower()):
            root.after(1000, animate_label)
            speak(user_text)
        if re.search("no", is_speaker_working.lower()):
            root.after(1000, animate_label)


def C_Day():
    day = datetime.today().weekday() + 1
    Day_dict = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        return str(day_of_the_week)


def c_time():
    string = datetime.now().strftime("%H:%M:%S")
    time_label.configure(text=string)
    time_label.after(1000, c_time)


def date():
    string = datetime.now().strftime("%d/%m/%Y")
    date_label.configure(text=string)
    date_label.after(1000, date)


@lru_cache
def temp():  # battery included
    IP = requests.get("https://api.ipify.org").text
    url = "https://get.geojs.io/v1/ip/geo/" + IP + ".json"
    geo_reqeust = requests.get(url)
    geo_data = geo_reqeust.json()
    city = geo_data["city"]
    string = Temp(city)
    temp_label.configure(
        text=f"The City {city} is Currently in a Temperature of {string}°C",
        font=(
            "Consolas",
            26,
        ),
    )
    temp_label.after(3600000, temp)


def computer_vision():
    os.system(
        f"{python_exe_location} {dir_agi}\\features\\Computer_Vision\\GUi.py"
    )


def chess():
    os.system(
        f"{python_exe_location} {dir_agi}\\features\\Chess\\ChessGame.py"
    )


def melody():
    os.system(
        f"{python_exe_location} {dir_agi}\\features\\melody_generator.py"
    )


def tictactoe():
    os.system(
        f"{python_exe_location} {dir_agi}\\features\\ticTactoe.py"
    )


def calculator():
    os.system(
        f"{python_exe_location} {dir_agi}\\features\\gui_apps\\calc.py"
    )


def status():
    os.system(
        f"{python_exe_location} {dir_agi}\\features\\gui_apps\\status.py"
    )


def earth():
    os.system(
        f"{python_exe_location} {dir_agi}\\features\\gui_apps\\earth.py"
    )


def iss():
    os.system(
        f"{python_exe_location} {dir_agi}\\features\\gui_apps\\Iss.py"
    )


coord_y = (height - 460) + -50


coord_y_1 = (height - 420) + -650
x = (width - 250) - 175

sidebar_frame = customtkinter.CTkFrame(
    root, width=175, height=550, corner_radius=30)
sidebar_frame.pack(pady=20)
sidebar_frame.place(x=10, y=(coord_y_1 + 325))


exit_button = customtkinter.CTkButton(
    master=sidebar_frame,
    text="Exit",
    command=exit,
    corner_radius=50,
    hover_color="red",
    font=("Consolas", 15),
    fg_color="transparent", border_width=1
)
exit_button.pack(pady=20)
exit_button.place(x=15, y=(coord_y_1 - -805))

text_label = customtkinter.CTkLabel(
    root, text=f"{random.choice(quotes)}", font=(my_font)
)
text_label.pack(pady=20)
text_label.place(x=550, y=200)

icon_button = customtkinter.CTkButton(
    sidebar_frame,
    text="Sleep Mode",
    command=icon_close,
    corner_radius=50,
    font=my_font_for_buttons,
    fg_color="transparent", border_width=1
)
icon_button.pack(pady=20)
icon_button.place(x=13, y=(coord_y_1 - -555))

status_button = customtkinter.CTkButton(
    sidebar_frame,
    text="Device Status",
    command=status,
    corner_radius=50,
    font=my_font_for_buttons,
    fg_color="transparent", border_width=1
)
status_button.pack(pady=20)
status_button.place(x=15, y=(coord_y_1 - -605))

time_label = customtkinter.CTkLabel(root, text="", font=("Consolas", 45))
time_label.pack(pady=30, padx=30)
time_label.place(x=(x + 150), y=50)  # 150
c_time()

temp_label = customtkinter.CTkLabel(root, text="")
temp_label.pack(pady=20)
temp_label.place(x=260, y=(coord_y + 350))
temp()

queries_widget = customtkinter.CTkTextbox(
    root, width=800, height=180, font=(
        "Consolas", 15), corner_radius=50)
queries_widget.pack(pady=20)
queries_widget.place(x=300, y=367)
button2_pressed = False


date_label = customtkinter.CTkLabel(root, text="", font=("Consolas", 30))
date_label.pack(pady=30, padx=30)
date_label.place(x=(x + 150), y=110)  # 210
date()

day_label = customtkinter.CTkLabel(root, text=C_Day(), font=("Consolas", 25))
day_label.pack(pady=30, padx=30)
day_label.place(x=(x + 150), y=155)  # 260

label_neuron = customtkinter.CTkLabel(
    root, text="Neuron", font=(
        "Ankh Sanctuary", 165), text_color="#41FDFE")
label_neuron.pack(pady=20)

earth_button = customtkinter.CTkButton(
    sidebar_frame,
    text="Earth 3D",
    font=my_font_for_buttons,
    command=earth,
    corner_radius=50,
    fg_color="transparent", border_width=1
)
earth_button.pack(pady=20)
earth_button.place(x=15, y=(coord_y_1 - -455))

iss_button = customtkinter.CTkButton(
    sidebar_frame,
    text="Iss Tracker",
    font=my_font_for_buttons,
    command=iss,
    corner_radius=50,
    fg_color="transparent", border_width=1
)
iss_button.pack(pady=20)
iss_button.place(x=15, y=(coord_y_1 - -505))

input_box = customtkinter.CTkEntry(
    root,
    width=420,
    height=75,
    placeholder_text="Type Your Question",
    font=("Consolas", 20),
    corner_radius=50,
)
input_box.pack(pady=20)

calc_button = customtkinter.CTkButton(
    sidebar_frame,
    text="Simple Calculator",
    command=calculator,
    corner_radius=50,
    font=my_font_for_buttons_2,
    fg_color="transparent", border_width=1
)
calc_button.pack(pady=20)
calc_button.place(x=15, y=(coord_y_1 - -310))

tictactoe_button = customtkinter.CTkButton(
    sidebar_frame,
    text="Tic Tac Toe",
    command=tictactoe,
    corner_radius=50,
    font=my_font_for_buttons,
    fg_color="transparent", border_width=1
)
tictactoe_button.pack(pady=20)
tictactoe_button.place(x=15, y=(coord_y_1 - -405))

comp_vis_button = customtkinter.CTkButton(
    sidebar_frame,
    text="Computer Vision",
    command=computer_vision,
    corner_radius=50,
    font=my_font_for_buttons_2,
    fg_color="transparent", border_width=1
)
comp_vis_button.pack(pady=20)
comp_vis_button.place(x=15, y=(coord_y_1 - -655))


def button2_command():
    global button2_pressed
    button2_pressed = True  # Set the variable to True when the button is pressed
    output()  # Call the output function


# Modify the button2 to use the button2_command
button2 = customtkinter.CTkButton(
    root,
    text="Send",
    text_color="white",
    command=lambda: output() and button2_command,  # Use the new command
    corner_radius=50,
    width=35,
    height=45,
    font=my_font_for_buttons,
    fg_color="transparent", border_width=1
)
button2.pack(pady=20)
button2.place(x=(x - 50), y=267)

chess_button = customtkinter.CTkButton(
    sidebar_frame,
    text="Chess",
    command=chess,
    corner_radius=50,
    font=my_font_for_buttons,
    fg_color="transparent", border_width=1
)
chess_button.pack(pady=20)
chess_button.place(x=15, y=(coord_y_1 - -355))


my_button = customtkinter.CTkButton(
    root,
    text="Change Light/Dark",
    command=change,
    corner_radius=50,
    font=my_font_for_buttons_2,
    fg_color="transparent", border_width=1
)
my_button.pack(pady=20)
my_button.place(x=22, y=(coord_y + 355))


if __name__ == "__main__":
    warnings.filterwarnings("ignore")

    import hashlib

    def md5(input_string):
        return hashlib.md5(input_string.encode()).hexdigest()

    with open(f"{dir_agi}\\data\\password.txt", "r+") as pwd:
        password = pwd.read()
        if password == "":
            new_password = pwinput("Please Type Your New Password -> ")
            pwd.write(md5(new_password))
            password = md5(new_password)
            pwd.close()

    user_entry = pwinput("Enter Your Password -> ")
    if md5(user_entry) == password:
        with open(f"{dir_agi}\\data\\age.txt", "r+") as file:
            age_file = file.read()
            if age_file == "":
                age = input("Age: ")
                age = md5(age)
                file.write(age)
                file.close()

            if md5(age_file) == md5("17") or md5("16") or md5("15") or md5("14") or md5("13") or md5("12") or md5("11") or md5(
                    "10") or md5("9") or md5("8") or md5("7") or md5("6") or md5("5") or md5("4") or md5("3") or md5("2") or md5("1") or md5("0"):
                age_safety.age_safety("N")

            if not md5(age_file) == md5("17") or md5("16") or md5("15") or md5("14") or md5("13") or md5("12") or md5("11") or md5(
                    "10") or md5("9") or md5("8") or md5("7") or md5("6") or md5("5") or md5("4") or md5("3") or md5("2") or md5("1") or md5("0"):
                age_safety.age_safety("Y")

        is_speaker_working = input(
            "Is The Speaker Working? Answer Properly Because This Will Affect Whether To Enable Speak Mode Or Not (yes or no answer these two options): ")
        root.mainloop()
        age_safety.age_safety(yesorno="Y")

    if md5(user_entry) != password:
        print("Wrong Password!")
        exit()
