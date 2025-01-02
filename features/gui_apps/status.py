import customtkinter as ctk
import psutil
import platform
import GPUtil

class SystemStatusApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("System Status")
        self.root.geometry("735x365")

        self.create_widgets()

        # Schedule the update_widgets function to be called every 1000 milliseconds (1 second)
        self.root.after(500, self.update_widgets)

    def create_widgets(self):
        label_frame = ctk.CTkFrame(self.root, corner_radius=0, width=550, height=600)
        label_frame.pack(padx=20, pady=20, anchor="nw")

        self.system_label = ctk.CTkLabel(label_frame, text="", font=("Consolas", 20), anchor="w")
        self.system_label.pack(fill="x", pady=5)

        self.machine_label = ctk.CTkLabel(label_frame, text="", font=("Consolas", 20), anchor="w")
        self.machine_label.pack(fill="x", pady=5)

        self.processor_label = ctk.CTkLabel(label_frame, text="", font=("Consolas", 20), anchor="w")
        self.processor_label.pack(fill="x", pady=5)

        self.cpu_usage_label = ctk.CTkLabel(label_frame, text="", font=("Consolas", 20), anchor="w")
        self.cpu_usage_label.pack(fill="x", pady=5)

        self.memory_usage_label = ctk.CTkLabel(label_frame, text="", font=("Consolas", 20), anchor="w")
        self.memory_usage_label.pack(fill="x", pady=5)

        self.disk_usage_label = ctk.CTkLabel(label_frame, text="", font=("Consolas", 20), anchor="w")
        self.disk_usage_label.pack(fill="x", pady=5)

        self.gpu_info_label = ctk.CTkLabel(label_frame, text="", font=("Consolas", 20), anchor="w")
        self.gpu_info_label.pack(fill="x", pady=5)

        self.battery_label = ctk.CTkLabel(label_frame, text="", font=("Consolas", 20), anchor="w")
        self.battery_label.pack(fill="x", pady=5)

    def update_widgets(self):
        self.system_label.configure(text=f"System: {platform.system()} {platform.release()} {platform.version()}")
        self.machine_label.configure(text=f"Machine: {platform.machine()}")
        self.processor_label.configure(text=f"Processor: {platform.processor()}")
        self.cpu_usage_label.configure(text=f"CPU Usage: {psutil.cpu_percent()}%")
        self.memory_usage_label.configure(text=f"Memory Usage: {psutil.virtual_memory().percent}%")
        self.disk_usage_label.configure(text=f"Disk Usage: {psutil.disk_usage('/').percent}%")

        try:
            gpus = GPUtil.getGPUs()
            gpu_info = ""
            for gpu in gpus:
                gpu_info += f"GPU {gpu.id}: {gpu.name} - {gpu.load * 100:.2f}%\n"
            self.gpu_info_label.configure(text=gpu_info)
        except:
            self.gpu_info_label.configure(text="No GPU found")

        if psutil.sensors_battery():
            battery = psutil.sensors_battery()
            self.battery_label.configure(text=f"Battery Percentage: {battery.percent}%")
        else:
            self.battery_label.configure(text="No battery found")

        # Schedule the update_widgets function to be called every 1000 milliseconds (1 second)
        self.root.after(1000, self.update_widgets)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = SystemStatusApp()
    app.run()