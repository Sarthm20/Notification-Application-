import time
from plyer import notification

if __name__== "__main__":
    while True:
        notification.notify(
            title="Please update your Windows System!!",
            message="Updated version of windows includes more features for windows based software also gives more security form varios viruses",
            timeout=12
            )

        time.sleep(60)
