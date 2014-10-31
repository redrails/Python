'''
This is like a fun thing I made to open reddit's RSS and then display the results in a list from with links.
It can do with a lot more work but it was quite fun to do.
- Need to append the Text widget with an error message if the input RSS feed is invalid.
Using feedparser class and Tkinter for GUI. 
'''

from Tkinter import *
import feedparser

root = Tk()
root.geometry('800x450+0+0')
root.title('Reddit RSS grabber!')


class WrapText(Text):

    def __init__(self, master, wraplength=50, **kw):
        Text.__init__(self, master, **kw)
        self.bind("<Any-Key>", self.check)
        self.wraplength = wraplength-1

    def check(self, event=None):
        line, column = self.index(INSERT).split('.')
        if event and event.keysym in ["BackSpace","Return"]: pass
        elif int(column) > self.wraplength:
            self.insert("%s.%s" % (line,column),"\n")

    def wrap_insert(self, index, text):
        for char in text:
            self.check()
            self.insert(index, char)

    def clear(self):
        self.delete(0.0, END)

    def contents(self):
        self.get(1.5,END)


class RSS():

    def __init__(self):
        self.titleGet = []
        self.linkGet = []

    def grabRSS(self, rssFeed):

        w.clear()

        self.rssFeed = rssFeed
        rss = feedparser.parse(self.rssFeed)

        for j in range(0,25):

            title = rss['entries'][j]['title']
            link = rss['entries'][j]['link']

            self.titleGet.append(title)
            self.linkGet.append(link)

        for i in range(0, len(self.titleGet)):

            w.wrap_insert(END,str(i+1)+". "+ self.titleGet[i]+"("+self.linkGet[i]+")\n--------------------\n")

w = WrapText(root, bg="white",wraplength=100, width=110)
w.pack()

e = Entry(root)
e.pack()
e.insert(0, "http://reddit.com/.rss")

def execRSS():
    rssCreator = RSS()
    if not w.contents():
        w.wrap_insert(END, "Not a valid RSS feed!")
    rssCreator.grabRSS(e.get())

buttonLeft = Button(root, text="GRAB RSS!", command=execRSS)
buttonLeft.pack()
buttonLeft.bind("<Button-1>", execRSS)

root.mainloop()
