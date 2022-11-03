import time

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



from_dir = r"C:\Users\USER\Desktop\Coding\PRO-C113\Images"
to_dir = r"C:\Users\USER\Desktop\Coding\PRO-C113\Images\New"

file_names = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(event)
        print(event.src_path)
        #Student Activity1
        name,extension = os.path.splitext(event.src_path)
        time.sleep(1)

        for key, value in file_names.items():
            time.sleep(1)
            if extension in value:
                file_name = os.path.basename(event.src_path)
                print('downloaded')
                path1 = from_dir + '/'+ file_name
                path2 = to_dir + '/' + key
                path3 =  to_dir + '/' + key + '/' + file_name

                if os.path.exists(path2):
                    print('moving the files')
                    shutil.move(path1,path3)
            
                else:
                    print('making a folder')
                    os.makedirs(path2)
                    print('mooving the files')
                    shutil.move(path1,path3)
    

    


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

#Student Activity2
try:
    while True:
        time.sleep(2)
        print('running')
except KeyboardInterrupt:
    print('stop')
    observer.stop()