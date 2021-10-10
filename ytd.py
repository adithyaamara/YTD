# importing packages
from pytube import YouTube
from prettytable import PrettyTable
import os

def convert(seconds):   #Convert time in seconds to human readable time
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    if hour == 0:
        return "%02d:%02d" % (minutes, seconds)  
    return "%d:%02d:%02d" % (hour, minutes, seconds)

link = [] # INITIALIZE LINK ARRAY FOR MULTI DOWNLOADS
# Read Links from file 
f = open("1.txt",'r')   # x.txt is always the name of file that contains youtube links one in one line.
for line in f:
    link.append(line)
print("Number of video links specified in file : ",len(link))
table = []
for i in range(len(link)):
    try:
        yt = YouTube(link[i])
    except Exception as e:
        print("Youtube Error : ",e)
    stream = yt.streams.filter(type = "audio",abr="128kbps").first()  #Applying audio 128 kbps filter
    #print(stream.__dict__)
    table.append([i+1, yt.title, int(((stream._filesize)/1048576)), convert(yt.length)])
    #print(i+1,":",yt.title,", Size in MB : ",int(((stream._filesize)/1048576)), "Duration in min- ",convert(yt.length))
t = PrettyTable(['Num', 'Name', 'Size', 'Duration'])
t.align = "l"
t.add_rows(table)
print(t)
input("Do you want to continue ???")
'''
# extract only audio
for item in yt.streams.filter(type = "audio",abr="128kbps"):
    print(item.__dict__)   # All attributes of item object
    print("Size in MB: ",int(((item._filesize)/1048576))) 


destination = "."

video = yt.streams.filter(type = "audio",abr="128kbps").first()
# download the file
out_file = video.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

# result of success
print(yt.title + " has been successfully downloaded.")
'''