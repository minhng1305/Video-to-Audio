from requests_html import HTMLSession
from pytube import YouTube
import pandas as pd 

def extract_url(url, url_list):
    session = HTMLSession()
    response = session.get(url)
    response.html.render(sleep=1, keep_page = True, scrolldown = 3)
    for links in response.html.find('a#video-title'):
        link = next(iter(links.absolute_links))

        #Check length of the video (< 5 mins and not live video)
        video = YouTube(link)
        leng = video.length
        if (0 < leng < 300):
            url_list.append(link)
        else:
            pass

def load_to_txt_file(list, new_file):
    file = open(new_file,'w')
    for url in list:
	    file.write(url+"\n")
    file.close()

def main():
    # Query the name of the person you want (short vids)
    name = input("Name: ")
    name_list = name.split()
    l = len(name_list)
    url = "https://www.youtube.com/results?search_query="
    for i in range(l):
        url = url+name_list[i]
        if i+1!=l:
            url += '+'
    url += "+short"
    
    # Extract youtube video links of that person into a list
    url_list = []
    extract_url(url, url_list)

    # Load that list into a new folder
    new_file = "new_url_file.txt"
    load_to_txt_file(url_list, new_file)

main()
