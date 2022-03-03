import json
# pytube, pytube3 version 12.0.0
from pytube import YouTube
from pytube.cli import on_progress

def downloadVideo(link):

  while(True):
    print("Choose one of the options\n"
          "1) Download highest quality Video\n"
          "2) Download highest quality mp4 Audio"
    )
    odabir = int(input())
    if (odabir == 1 or odabir == 2): break

  print("Starting download...")
  try: 
    yt = YouTube(link, on_progress_callback=on_progress)
    if odabir == 1:
      stream = yt.streams.get_highest_resolution()
    else:
      stream = yt.streams.get_audio_only()
    stream.download()
  
    print(f'Downloaded |||{yt.title}|||')
  
  except: 
        
      #to handle exception 
      print("Connection Error")
      print(f'FAILED download of {yt.title}')
  

def downloadList():
  f = open("JSONLinks.txt", "r")
  mystr = ''
  for x in f:
    mystr += x
  #link of the video to be downloaded   
  link = json.loads(mystr)
  f.close()
  counter = 0

  while(True):
    print("Choose one of the options\n"
          "1) Download highest quality Videos\n"
          "2) Download highest quality mp4 Audio files"
    )
    odabir = int(input())
    if (odabir == 1 or odabir == 2): break

  print("Starting download...")
  for i in link: 
      try: 
        yt = YouTube(i, on_progress_callback=on_progress)      
        if odabir == 1:
          stream = yt.streams.get_highest_resolution()
        else:
          stream = yt.streams.get_audio_only()
        stream.download()
        counter += 1
        print(f'Downloaded||| {yt.title}|||\nNumber of downloaded files:{counter}/{len(link)}')
      
      except: 
            
          #to handle exception 
          print("Connection Error")
          print(f'FAILED download of {yt.title}')



print("Youtube downloader 1.0 by Tin Pritisanac")

while(True):
  print("Choose one of the options\n"
        "1) Download single video/audio file\n"
        "2) Download multiple files from links in JSONLinks.txt"
  )
  odabir = int(input())
  if (odabir == 1 or odabir == 2): break

if odabir == 1:
  link = input("Paste YT video link:\n")
  downloadVideo(link)
else: 
  downloadList()

 
input("Finished downloads!")