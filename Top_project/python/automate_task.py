
from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep
from win11toast import toast



import logging
import os
print("PID of manager file is:")
print(os.getpid())

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#POP up when code runs 25 sec
toast("File manager started!","this pop up is live for 25 seconds", duration="long", button='Dismiss')

# ! FILL IN BELOW
# ? folder to track e.g. Windows: "C:\\Users\\UserName\\Downloads"
source_dir = "C:/Users/Lenovo/Downloads"
dest_dir_video = "C:/Users/Lenovo/Desktop/Videos"
dest_dir_image = "C:/Users/Lenovo/Desktop/Image"
dest_dir_documents = "C:/Users/Lenovo/Desktop/Docs"

# ? supported image types
image_extensions = [".jpg", ".jpeg",  ".png", ".gif", ".webp",]
# ? supported Video types
video_extensions = [".webm",  ".mpeg", ".mpv",
                    ".mp4",".avi", ".wmv", ".mov",]


# ? supported Document types
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]



def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name


def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)

 #? Filekeeper is the class which dealing the files and moving them  from source

class Filekeeper(FileSystemEventHandler):
    # ? THIS FUNCTION WILL RUN WHENEVER THERE IS A CHANGE IN "source_dir"
    # ? .upper is for not missing out on files with uppercase extensions
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_files(entry, name)

   

    def check_video_files(self, entry, name):  # * Checks all Video Files
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move_file(dest_dir_video, entry, name)
                logging.info(f"Moved video file: {name}")

    def check_image_files(self, entry, name):  # * Checks all Image Files
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move_file(dest_dir_image, entry, name)
                logging.info(f"Moved image file: {name}")

    def check_document_files(self, entry, name):  # * Checks all Document Files
        for documents_extension in document_extensions:
            if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
                move_file(dest_dir_documents, entry, name)
                logging.info(f"Moved document file: {name}")


# ! NO NEED TO CHANGE BELOW CODE
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = Filekeeper()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
