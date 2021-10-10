# importing packages
from pytube import YouTube
from prettytable import PrettyTable
import os
import datetime

# Download Config
destination = "./downloads"
filename = "1.txt"
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
f = open(filename,'r')   # x.txt is always the name of file that contains youtube links one in one line.
for line in f:
    link.append(line)
print("Number of video links specified in file : ",len(link))
good_links = []   
bad_links = []
t_good = PrettyTable(['Num', 'Name', 'Size', 'Duration', 'Link'])  #PrettyTable formatting
t_bad = PrettyTable(['Num','Link','Error'])
for i in range(len(link)):
    try:
        yt = YouTube(link[i])
        stream = yt.streams.filter(type = "audio",abr="128kbps").first()  #Applying audio 128 kbps filter
        #print(stream.__dict__)
        good_links.append([i+1, yt.title, int(((stream._filesize)/1048576)), convert(yt.length), link[i]])
        #print(i+1,":",yt.title,", Size in MB : ",int(((stream._filesize)/1048576)), "Duration in min- ",convert(yt.length))
    except Exception as e:
        #print("Youtube Error : ",e)
        bad_links.append([str(i+1), str(link[i]), e])
        continue
if(len(good_links)!=0):
    t_good.align = "l"
    t_good.add_rows(good_links)
    t_good.del_column('Link')
    print("Good Links --> ")
    print(t_good)
if len(bad_links)!=0:
    t_bad.align = "l"
    t_bad.add_rows(bad_links)
    print("Bad Links --> ")
    print(t_bad)
# Proceed to download choice
choice = input("Do you want to continue downloading all valid links (" + str(len(good_links)) + ") - Y / N ???")
if choice == 'Y' or 'y':
    start = datetime.datetime.now()
    for i in range(len(good_links)):
        try:
            yt = YouTube(good_links[i][4])
            stream = yt.streams.filter(type = "audio",abr="128kbps").first()  # Applying audio 128 kbps filter
        
            # download the file
            out_file = stream.download(output_path=destination)
            
            # save the file
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            # result of success
            print(yt.title + " has been successfully downloaded.")
        
        except Exception as e:
            print("Error Downloading file -> ",yt.title)
            continue
    finish = datetime.datetime.now()
    total = len(good_links)
    time_taken = finish - start
    time = convert(time_taken.seconds)
    print(f'Finished Downloading {total} files in {time} time!!')    
else:
    print("Thank you for using this tool...")