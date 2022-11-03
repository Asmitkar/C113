import time

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = r"C:\Users\USER\Desktop\Coding\PRO-C113"


class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created")
    def on_deleted(self, event):
        print('file deleted')
    def on_modified(self, event):
        print('file modified')
    def on_moved(self, event):
        print('file moved')


# Initialize Event Handler Class
event_handler = FileEventHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print('running')
except KeyboardInterrupt:
    print('stop')
    observer.stop()
