from tkinter import *
from PIL import Image,ImageTk
import pygame
from random import *
#tkinter: To display music player
#PIL: To display image on button
#pygame: To play songs
#random: To execute shuffle button

#Circular Doubly Linked List
class node:
    def __init__(self,audio_name,photo_name,name):
        self.audio_name=audio_name
        self.photo_name=photo_name
        self.name=name
        self.next=None
        self.prev=None

class linkedlist:
    def __init__(self):
        self.head=None
    def insert_end(self,new1,new2,new3):
        new=node(new1,new2,new3)
        new.next=None
        if self.head==None:
            new.prev=None
            self.head=new
            new.next=new
            return
        t=self.head
        while(t.next!=self.head):
            t=t.next
        t.next=new
        new.prev=t
        new.next=self.head
        self.head.prev=new
l2=list()
def printlist(l):
    t=l.head
    while(t.next!=l.head):
        l2.append(t.audio_name)
        t=t.next
    l2.append(t.audio_name)

# l is the object of linked list 
l=linkedlist()
l.insert_end('chitti.mp3','chitti_img.png','Chitti song from Jathiratnalu')
l.insert_end('Arere_Vaanaa.mp3','Awaara.png','Arere vaana from Awaara')
l.insert_end('Ay_Pilla.mp3','Ay_pilla.png','Ay pilla from Love story')
l.insert_end('Chiru_chiru.mp3','Awaara.png','Chiru chiru from Awaara')
l.insert_end('Nenu_Nuvvantu.mp3','orange.png','Nenu nuvvantu from Orange')
l.insert_end('Rooba_Rooba.mp3','orange.png','Rooba rooba from Orange')
printlist(l)

#play button image
def play_button():
    image_play = Image.open("play.png")
    resize_play_image = image_play.resize((30, 30),Image.ANTIALIAS)
    photo_play = ImageTk.PhotoImage(resize_play_image)
    return photo_play

#shuffle songs
def shuffle_songs(top_loop):
    name=choice(l2)
    loop(name,top_loop)

#pause button image
def pause_button():
    image_pause = Image.open("pause.png")
    resize_pause_image = image_pause.resize((30, 30),Image.ANTIALIAS)
    photo_pause = ImageTk.PhotoImage(resize_pause_image)
    return photo_pause

#exit button image
def exit_button():
    image_stop = Image.open("stop.png")
    resize_stop_image = image_stop.resize((30, 30),Image.ANTIALIAS)
    photo_stop = ImageTk.PhotoImage(resize_stop_image)
    return photo_stop

#next button image
def next_button():
    image_next = Image.open("next.png")
    resize_next_image = image_next.resize((30, 30),Image.ANTIALIAS)
    photo_next = ImageTk.PhotoImage(resize_next_image)
    return photo_next

#previous button image
def prev_button():
    image_prev = Image.open("prev.png")
    resize_prev_image = image_prev.resize((30, 30),Image.ANTIALIAS)
    photo_prev = ImageTk.PhotoImage(resize_prev_image)
    return photo_prev

#next method
def next1(audio,top_loop):
    ptr=l.head
    while True:
        if ptr.audio_name==audio:
            ptr=ptr.next
            audio=ptr.audio_name
            break
        ptr=ptr.next
    loop(audio,top_loop)

#previous method
def prev1(audio,top_loop):
    ptr=l.head
    while True:
        if ptr.audio_name==audio:
            ptr=ptr.prev
            audio=ptr.audio_name
            break
        ptr=ptr.prev
    loop(audio,top_loop)

#loop method: Main method
def loop(audio,top_loop):
    if top_loop.winfo_exists()==0:
        top_loop=Toplevel()
    #deiconify is used to restore toplevel window
    top_loop.deiconify()
    #To unpause audio
    def loop_unpause():
        pygame.mixer.music.unpause()
        pause=Button(top_loop,bg='#b0ff66',activebackground='#99ffcc',image=photo_pause,command=loop_pause).place(x=150,y=280)
    #To pause audio
    def loop_pause():
        pygame.mixer.music.pause()
        play=Button(top_loop,bg='#b0ff66',activebackground='#99ffcc',image=photo_play,command=loop_unpause).place(x=150,y=280)

    ptr=l.head
    while 1:
        if ptr.audio_name==audio:
            photo=ptr.photo_name
            song=ptr.name
            break
        ptr=ptr.next
    
    top_loop.title(song)
    top_loop.geometry('400x400')
    
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    
    #Song image
    image_loop= Image.open(photo)
    resize_loop_image = image_loop.resize((250, 250),Image.ANTIALIAS)
    photo_loop= ImageTk.PhotoImage(resize_loop_image)
    photo_loop_label=Label(top_loop,image=photo_loop).place(x=85,y=20)
    # destroy method is to stop playing the music
    def destroy():
        pygame.mixer.music.stop()
        top_loop.destroy()
    #pause button
    photo_pause=pause_button()
    pause=Button(top_loop,bg='#b0ff66',activebackground='#99ffcc',image=photo_pause,command=loop_pause).place(x=150,y=280)
    #exit button
    exit1=exit_button()
    stop=Button(top_loop,bg='#b0ff66',activebackground='#99ffcc',image=exit1,command=destroy).place(x=230,y=280)
    #next button
    photo_next=next_button()
    next=Button(top_loop,bg='#b0ff66',activebackground='#99ffcc',image=photo_next,command=lambda:next1(audio,top_loop)).place(x=190,y=280)
    #previous button
    photo_prev=prev_button()
    prev=Button(top_loop,bg='#b0ff66',activebackground='#99ffcc',image=photo_prev,command=lambda:prev1(audio,top_loop)).place(x=110,y=280)
    
    top_loop.mainloop()

#Main Window    
window=Tk()
window.title('Music Player')
window.geometry('500x500')
window.configure(bg='#99ffcc')

#Toplevel window
top_loop=Toplevel(window)
top_loop.configure(bg='#f2ffe6')

#withdraw is used to hide toplevel window
top_loop.withdraw()

#Heading Label
heading=Label(text='PLAYLIST',font='Colus',bg='#262626',fg='#ffffff',width=20,relief=GROOVE,borderwidth=10).place(x=140,y=20)

#Shuffle image button
image = Image.open("shuffle.png")
resize_shuffle_image = image.resize((20, 20))
photo_shuffle = ImageTk.PhotoImage(resize_shuffle_image)
shuffle=Button(text='Shuffle',fg='#003300',bg='#99ff99',activebackground='#000000',activeforeground='#ffffff',image=photo_shuffle,compound=BOTTOM,height=38,command= lambda:shuffle_songs(top_loop)).place(x=430,y=80)

#Song1 
song1=Label(text='1. Chitti song from Jathiratnalu                           ',font='Colus',bg='#ddff99').place(x=0,y=150)
photo_play=play_button()
play=Button(bg='#99ff99',activebackground='#99ffcc',image=photo_play,command=lambda: loop('chitti.mp3',top_loop))
play.place(x=430,y=148)

#song2
song2=Label(text='2. Arere vaana from Awaara                               ',font='Colus',bg='#ddff99').place(x=0,y=200)
play=Button(bg='#99ff99',activebackground='#99ffcc',image=photo_play,command=lambda: loop('Arere_Vaanaa.mp3',top_loop)).place(x=430,y=196)

#song3
song3=Label(text='3. Ay pilla from Love story                                    ',font='Colus',bg='#ddff99').place(x=0,y=250)
play=Button(bg='#99ff99',activebackground='#99ffcc',image=photo_play,command=lambda: loop('Ay_Pilla.mp3',top_loop)).place(x=430,y=246)

#song4
song4=Label(text='4. Chiru chiru from Awaara                                   ',font='Colus',bg='#ddff99').place(x=0,y=300)
play=Button(bg='#99ff99',activebackground='#99ffcc',image=photo_play,command=lambda: loop('Chiru_chiru.mp3',top_loop)).place(x=430,y=296)

#song5
song5=Label(text='5. Nenu nuvvantu from Orange                             ',font='Colus',bg='#ddff99').place(x=0,y=350)
play=Button(bg='#99ff99',activebackground='#99ffcc',image=photo_play,command=lambda: loop('Nenu_Nuvvantu.mp3',top_loop)).place(x=430,y=346)

#song6
song6=Label(text='6. Rooba rooba from Orange                             ',font='Colus',bg='#ddff99').place(x=0,y=400)
play=Button(bg='#99ff99',activebackground='#99ffcc',image=photo_play,command=lambda: loop('Rooba_Rooba.mp3',top_loop)).place(x=430,y=396)

window.mainloop()
