import customtkinter
import warnings
dir_agi = "\\Neuron_App"
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme(f"{dir_agi}\\images\\cyan.json")
warnings.filterwarnings("ignore")
root = customtkinter.CTk()
root.resizable(False, False)
root.geometry("250x300")

def expression():
    os.system(
        f"C:/Users/jinuv/AppData/Local/Programs/Python/Python312/python.exe d:/Version_2_Jarvis/Computer_Vision/expression_tracker.py"
    )

def eyes():
    os.system(
        f"C:/Users/jinuv/AppData/Local/Programs/Python/Python312/python.exe d:/Version_2_Jarvis/Computer_Vision/eye_tracker.py"
    )

def face():
    os.system(
        f"C:/Users/jinuv/AppData/Local/Programs/Python/Python312/python.exe d:/Version_2_Jarvis/Computer_Vision/face_tracker.py"
    )

def object():
    os.system(
        f"C:/Users/jinuv/AppData/Local/Programs/Python/Python312/python.exe d:/Version_2_Jarvis/Computer_Vision/object_detection.py"
    )

computer_label = customtkinter.CTkLabel(root, text="Computer Vision", font=("Consolas", 20))
computer_label.pack(pady=20)
computer_label.place(x=41, y=20)

expression_button = customtkinter.CTkButton(root, text="Expression Tracker", font=("Consolas", 15), command=expression)
expression_button.pack(pady=20)
expression_button.place(x=38, y=250)

eyes_button = customtkinter.CTkButton(root, text="Eyes Tracker", font=("Consolas", 15), command=eyes)
eyes_button.pack(pady=20)
eyes_button.place(x=46, y=200)

face_button = customtkinter.CTkButton(root, text="Face Tracker", font=("Consolas", 15), command=face)
face_button.pack(pady=20)
face_button.place(x=46, y=150)

object_button = customtkinter.CTkButton(root, text="Object Detector", font=("Consolas", 15), command=object)
object_button.pack(pady=20)
object_button.place(x=46, y=100)

if __name__ == '__main__':
    root.mainloop()