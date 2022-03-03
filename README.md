# YoutubeDownloader
My Youtube video downloader in Python

# How to use
## 1.  If you want to download single video
1.  Run YouTubeDownloader1.0
2.  Choose option 1) by entering 1
3.  Paste the video link and hit enter!
4.  Video will be downloaded in the same directory as the script file in the **highest quality available**

## 2. Downloading multiple videos
### 1.  If you want to get the links from the youtube channel
  - Go to the desired channel
  - Make sure all the videos to be downloaded are shwon on the page (for **all videos** scroll all the way down until there are no more videos to be loaded on the page)
  - Open GetLinksFromChannel.txt, copy the code from the file
  - Open dev tools in the browser, go to console and paste the copied code. Hit enter.
  - Copy all the links printed in the console and save it in the file JSONLinks.txt
  - JSONLinks.txt file must be in the same folder as the YouTubeDownloader1.0
  - Run YouTubeDownloader1.0 and choose option 2
 ### 2. If you have all the links that you want to download
  - Save the links in the file JSONLinks.txt in the following format (like a pyton LIST):
 
```
["https://www.youtube.com/watch?v=wTP2RUD_cL0", "https://www.youtube.com/watch?v=kd9TlGDZGkI", "https://www.youtube.com/watch?v=Vppbdf-qtGU"]
```
  - Run YouTubeDownloader1.0 and choose option 2
