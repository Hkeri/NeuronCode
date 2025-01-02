import psutil
import requests

class HealthCare:
    '''
    
    Health Care CheckUp In Python, is it such a beauty!

    '''
    def internet_status(timeout=5):
        try:
            requests.get("https://www.google.com", timeout=timeout)
            return "Internet Positive"
        except ConnectionError:
            return "Internet Negative"

    def network_traffic(threshold=100):
        if HealthCare.internet_status():
            network_traffic = psutil.net_io_counters().bytes_recv +\
                            psutil.net_io_counters().bytes_sent
            network_traffic = ((network_traffic / 1024) / 1024)
            if (int(network_traffic) + 1) >= threshold:
                message = f"High network traffic detected: {network_traffic:.2f} MB"
                return str(message)
            
            if (int(network_traffic) - 1) <= threshold:
                message = f"No Network Traffic Detected: {network_traffic:.2f} MB"
                return str(message)
        if not HealthCare.internet_status():
            return "There Is Currently No Internet!"

    def cpu_usage():
        c = int(psutil.cpu_percent(1))
        if c < 75:
            return f"CPU Usage is Safe by {c}%"
        
        if c > 75:
            return f"CPU USAGE IS EXCEEDING! CPU is Rapidly in {c}%"

    def disk_usage(disk="/"):
        if (psutil.disk_usage(disk).percent) >= 75:
            return f"Disk Usage is Currently {psutil.disk_usage(disk).percent}. Please Clean Your Junk Files"
        
        if (psutil.disk_usage(disk).percent) <= 75:
            return f"Disk Usage is Normal by {psutil.disk_usage(disk).percent}"

    def ram_usage():
        r = int(psutil.virtual_memory().percent)
        if (r) >= 75:
            return f"RAM USAGE IS EXCEEDING! Ram Usage is Currently {r}%"
        
        if (r) <= 75:
            return f"Ram Usage is Normal By {r}%"
    
    def grand_finale():
        return f"{HealthCare.cpu_usage()}, \n{HealthCare.ram_usage()}, \n{HealthCare.disk_usage()}, \n{HealthCare.network_traffic()}"

   