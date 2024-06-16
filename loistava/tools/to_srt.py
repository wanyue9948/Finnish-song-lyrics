import datetime,os

def format_time(seconds):
    """Format seconds to SRT timestamp format"""
    td = datetime.timedelta(seconds=seconds)
    d = datetime.datetime(1, 1, 1) + td
    return f"{d.hour:02}:{d.minute:02}:{d.second:02},000"

def lyrics_to_srt(lyrics_file, srt_file):
    with open(lyrics_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    srt_content = []
    counter = 1
    time_counter = 24  # start time

    duration = 3  # duration of each subtitle in seconds
    gap = 1  # gap between subtitles in seconds

    for line in lines:
        line = line.strip()
        if line:
            start_time = format_time(time_counter)
            end_time = format_time(time_counter + duration)
            srt_content.append(f"{counter}")
            srt_content.append(f"{start_time} --> {end_time}")
            srt_content.append(line)
            srt_content.append("")  # Blank line to separate subtitles

            counter += 1
            time_counter += duration + gap  # Move the time counter forward correctly

    with open(srt_file, 'w', encoding='utf-8') as file:
        file.write("\n".join(srt_content))

# Define the file paths
current_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the current script
parent_dir = os.path.dirname(current_dir)  # Parent directory

lyrics_file = os.path.join(parent_dir,"suomea.txt")
srt_file = os.path.join(parent_dir,"suomea.srt")
lyrics_to_srt(lyrics_file, srt_file)