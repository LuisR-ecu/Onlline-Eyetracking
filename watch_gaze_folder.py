import time
import glob
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith('.xlsx'):
            print(f"📁 New Excel file detected: {event.src_path}")
            os.system("python3 analyze_data.py")

if __name__ == "__main__":
    path = "gaze_data/"
    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    print("👁 Watching gaze_data/ for new files... Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()