import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir ="C:\Users\paczi\Downloads\Proyecto 101"

class FilesEventHandler(FileSystemEventHandler):

    def on_created(self,event):
        print(f"¡oye,{event.src_path} ha side creado!")

    def on_deleted(self, event):
        print(f"¡lo siento! ¡Alguien borró {event.src_path}!")

    def on_moved(self, event):
        print(f"{event.src_path} se fue de esta carpeta!")

    def on_modified(self, event):
        print(f"¡lo siento! ¡ {event.src_path} fue modificado!")


event_handler=FilesEventHandler()

observer=Observer()

observer.schedule(event_handler,from_dir,recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("ejecutando...")
except KeyboardInterrupt:
    print("detenido")
    observer.stop()