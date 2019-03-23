#!/usr/bin/python2.6 -tt
import sys
import os
import re
#import wx
#import cl
#import pygame.mixer
from tkinter import *

class Mome:
  keygen=["0","0"]
  def mome(self,filename,Input):
	#previne redundancia real
    #if self.keygen[1]==Input:
      #return self.keygen[0]
    try:
      f=open(filename,'rU')
    except IOError:
      print ('IOError %s' % filename)
      exit()
    for line in f:
      line=line[:-1]
      item=line.split('	')
      keyfound=(item[0]==self.keygen[0] and item[1]==Input) #Bool
      if keyfound:
        #MOME UPDATE
        self.keygen[0]=item[2]
        self.keygen[1]=Input
        f.close()
        break
    return self.keygen[0]
    
class Gui():
  def __init__(self):
    app = Tk()
    app.title("MOME")
    app.geometry('200x100+200+100')
    Gui.gui_output=StringVar()
    #self.gui_input=StringVar()
    Gui.gui_output.set("empty")
    #self.gui_input.set("empty")
    Label(app,text="Entry: ").pack()
    Gui.textfield=Entry(app)
    Gui.textfield.pack()
    Button(app,text="Enter",command=__save_data).pack()
    l1=Label(app,textvariable=Gui.gui_output,height=10)
    l1.pack(side='left')
    app.mainloop()

def _Gui__save_data():
  data=Gui.textfield.get()
  #print ("entrada %s" % data)
  if data==None:
    data="Enter"
  Gui.textfield.delete(0,END)
  Gui.gui_output.set(Mome().mome(filename,data))#instance overflow ?
  print ("output %s" % Gui.gui_output.get())
  
if __name__=='__main__':
  
  filename="file-2.txt"
  
  app_1=Gui()
