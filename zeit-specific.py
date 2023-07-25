# python run code at specific time
# To run Python code at a specific time
# search of the library
# schedule


'''
import schedule
import time     # AttributeError: partially initialized module 'schedule' has no attribute 'every' (most likely due to a circular import)
                # es gab fehler, weil ich den Name von dem file time genannt habe.

def job():
    print("I'm working...")

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

'''
'''
import schedule
import time

def job():
    print("I am anas")

schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
'''


# python show mac and windows notification
# with plyer
'''
from plyer import notification

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Notification will automatically close after 10 seconds
    )

# Example usage
show_notification("Hello", "This is a notification!")
'''



'''
# show mac and windows notification at a specific time

import schedule
import time
from plyer import notification



def job():
    def show_notification(title, message):
        notification.notify(
            title=title,
            message=message,
            timeout=1  # Notification will automatically close after 10 seconds
        )


show_notification("Hello", "This is a anas notification!")
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

'''