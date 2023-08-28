from pytube import YouTube

def extract_to_audio(url, filepath):
    try:
        video = YouTube(url)     
        stream = video.streams.filter(only_audio=True).first()
        stream.download(filepath)
        print("The video is downloaded in mp4.")
    except KeyError:
        print("Unable to fetch video information. Please check the video URL or your network connection.")

def main():
    file = open("/Users/mac/Desktop/Projects/Audio-to-text_Project/new_url_file.txt", 'r')
    url_list = file.readlines()
    
    # Read url from text file
    for url in url_list:
        url = url.strip()
        filepath = f"/Users/mac/Desktop/Projects/Audio-to-text_Project/audio"
        extract_to_audio(url, filepath)

main()
