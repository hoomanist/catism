'''
this a api and Tkinter training 
author : hooman
Welcome to my world
Recovery old stuff from someone github
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
    r=requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2')
    json_response=r.json()[0]
    text=json_response['text']
    w.config(text=text)
btn = Button(window ,text = 'Next' , command=clicked) 
btn.pack()
window.geometry('1200x200')
window.mainloop()
