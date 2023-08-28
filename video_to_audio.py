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
    file = open("new_url_file.txt", 'r')
    url_list = file.readlines()
    
    # Read url from text file
    for url in url_list:
        url = url.strip()
        filepath = "file path"
        extract_to_audio(url, filepath)

main()
