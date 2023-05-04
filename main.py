import time
from plyer import notification

if __name__ =="__main__":
    while True:
        notification.notify(
            title = "HEY BOSS!! Please drink water now.",

            message = "It is the time to drink water. I will inform you after every two hours.",

            app_icon = "C:\Sairaj Joshi\My Projects (Local)\Desktop Notification System (Python)\glass_icon.ico",

            timeout = 6

            

        )

        # program will run after every 2 hours
        time.sleep(60*120)  # ------ 60 SECONDS x 120 SECONDS = 2 HOURS
