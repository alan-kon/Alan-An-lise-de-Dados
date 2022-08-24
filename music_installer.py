import urllib.request
import re
from pytube import YouTube
from tkinter import *
import os

path = r"C:\Users\alanb\Downloads\GitHub\Dev.Alan"       # Path where your new music folder is gonna be     (E.g.: r"C:\Users\[your_pc_user]\Desktop")
directory = "Downloaded musics"   # Name of the folder to allocate the musics        (E.g: "Downloaded musics")


global x 
x= 0

def get(listen):
    os.chdir(path)
    path2= f"{path}\{directory}"
    
    if os.path.isdir(path2):
        global x
        x+=1
        musica = str(Musica.get())
        musica = re.sub(r"\s+", "", musica)
        
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+musica)
        
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        print(video_ids)

        url = f"https://www.youtube.com/watch?v={video_ids[0]}"

        yt = YouTube(url)
        print(yt.title)
        stream = yt.streams.filter(only_audio = True)[0]
        stream.download(path2)
        musica = (yt.title).replace(".","").replace(",","").replace(":","").replace("#","").replace("@","")
        musica= musica.replace("?","").replace("!","").replace("|", "")
        file = f"{path2}\{musica}.mp4"
        print(file)
        
        if listen == 1: os.startfile(file)
        
        if os.path.exists(file):
            x+=1
            Label(frame, bg="green",text="BAIXADO: ").grid(row=x,column=2)
            Label(frame,text=yt.title+".mp4").grid(row=x,column=3)
            if listen == 1: os.startfile(file)
        else: Label(frame,bg="red", text="Não baixou").grid(row=x,column=2)
        
    else:
        os.mkdir(directory)
        Label(window, text="Pasta criada na Área de Trabalho\nClique novamente para baixar e ouvir").grid(row=5, column=1)
        
def delete():
    Musica.delete(0, 'end')
    frame.destroy()
    criar_frame()


window = Tk()
Label(window, text = "Digite a música que você quer baixar:").grid(row= 0)

Musica = Entry(window)
Musica.grid(row=1)

frame = Frame(window)
frame.grid(row=3)

Button(window, text= "Baixar", command=lambda: get(0)).grid(row=1,column=1)
Button(window, text= "Baixar e ouvir agora", command=lambda: get(1)).grid(row=2,column=1)
Button(window, text= "Limpar histórico de Downloads", command= delete).grid(row=3, column= 1)

def criar_frame():
    global frame
    frame= frame = Frame(window)
    frame.grid(row=3)

window.mainloop()