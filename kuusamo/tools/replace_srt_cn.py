import re, os

def read_srt(file_path):
    """Read the SRT file and extract time codes and subtitles"""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the content into individual subtitle blocks
    blocks = re.split(r'\n\n+', content.strip())
    
    subtitles = []
    for block in blocks:
        parts = block.split('\n', 2)
        if len(parts) == 3:
            index, timecode, subtitle = parts
            subtitles.append((timecode, subtitle))
    
    return subtitles

def read_lyrics(file_path):
    """Read the English lyrics file and return the lines"""
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines if line.strip()]

def write_srt(subtitles, lyrics, output_path):
    """Write the new subtitles to a new SRT file"""
    with open(output_path, 'w', encoding='utf-8') as file:
        for i, (timecode, _) in enumerate(subtitles):
            file.write(f"{i + 1}\n")
            file.write(f"{timecode}\n")
            if i < len(lyrics):
                file.write(f"{lyrics[i]}\n\n")
            else:
                file.write("\n")

# Define the file paths
current_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the current script
parent_dir = os.path.dirname(current_dir)  # Parent directory

srt_file = os.path.join(parent_dir, "newsuomea.srt")
lyrics_file = os.path.join(parent_dir, "kiina.txt")
output_srt_file = os.path.join(parent_dir, "kiina.srt")

# Read the SRT file and English lyrics
subtitles = read_srt(srt_file)
lyrics = read_lyrics(lyrics_file)

# Write the new SRT file with English lyrics
write_srt(subtitles, lyrics, output_srt_file)
