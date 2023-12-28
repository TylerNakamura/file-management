import os
import datetime
from PIL import Image
from moviepy.editor import VideoFileClip

def get_earliest_date(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    earliest_dates = {}

    for file in files:
        print(f"Processing file: {file}")  # Debug print

        file_path = os.path.join(directory, file)

        if file.lower().endswith('.jpg'):
            try:
                with Image.open(file_path) as img:
                    exif_data = img._getexif()
                    creation_time = exif_data.get(36867)
                    if creation_time:
                        earliest_time = datetime.datetime.strptime(creation_time, '%Y:%m:%d %H:%M:%S')
                        earliest_dates[file] = earliest_time
            except (AttributeError, KeyError, IndexError):
                earliest_dates[file] = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))

        elif file.lower().endswith('.mov'):
            try:
                clip = VideoFileClip(file_path)
                creation_time = clip.reader.metadata.get('creation_time')
                if creation_time:
                    earliest_time = datetime.datetime.strptime(creation_time, '%Y-%m-%d %H:%M:%S')
                    earliest_dates[file] = earliest_time
                clip.close()
            except Exception as e:
                earliest_dates[file] = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))

        else:
            earliest_dates[file] = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))

    return earliest_dates

# Replace 'your_directory_path' with the path to your directory
directory_path = '/app/src'

if os.path.exists(directory_path) and os.path.isdir(directory_path):
    print("Scanning directory...")  # Debug print
    earliest_dates = get_earliest_date(directory_path)
    for file, date in earliest_dates.items():
        formatted_date = date.strftime('%Y-%m-%d')  # Adjust the format here
        new_name = f"{formatted_date}-{file}"
        os.rename(os.path.join(directory_path, file), os.path.join(directory_path, new_name))
        print(f"Renamed: {file} to {new_name}")
else:
    print("Directory not found.")
