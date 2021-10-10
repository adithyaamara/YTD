from tkinter import *
from ytd import main

r = Tk()
r.title('Youtube Downloader')
v = IntVar()
Label(r,text="File format -> ").pack()
Radiobutton(r, text='MP3', variable=v, value=1).pack()
Radiobutton(r, text='MP4', variable=v, value=2).pack()
Button (r, text="Submit", command=r.destroy).pack()
r.mainloop()

if v.get() == 1:
    main("audio")
else:
    main("video")

