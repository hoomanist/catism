'''
this a api and tkinter training 
author : hooman
'''
# import libraries
import requests
import sys
from tkinter import *
#get info about cats
r=requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2')
json_response=r.json()[0]
text=json_response['text']
#a gui for show info
window=Tk()
window.title('catism : cats fact')
w=Label(window,text=text)
w.pack()
def clicked():
    exit(1)
btn = Button(window ,text = 'commit' , command=clicked) 
btn.pack()
window.geometry('1200x200')
window.mainloop()
