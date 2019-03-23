#!/usr/bin/python2.6 -tt
import sys
import os
import re
#import pygame.mixer
from Tkinter import *

class MOME:
  keygen=[]
  inicdata="0"
  def __init__(self,filename,inicdata):
    self.keygen=["0","0"]
    self.MOME(filename,inicdata)
  def MOME(self,filename,Input):
    #if self.keygen[1]==Input:
      #return self.keygen[0]
    try:
      f=open(filename,'rU')
    except IOError:
      print 'IOError',filename
      exit()
    for line in f:
      line=line[:-1]
      item=line.split('-')
      keyfound=(item[0]==self.keygen[0] and item[1]==Input) #Bool
      if keyfound:
        #MOME UPDATE
        self.keygen[0]=item[2]
        self.keygen[1]=Input
        f.close()
        break
    return self.keygen[0]
    
class GUI:
  def __init__(self):
    app = Tk()
    app.title("MOME")
    app.geometry('200x100+200+100')
    self.gui_output=StringVar()
    self.gui_input=StringVar()
    self.gui_output.set("empty")
    self.gui_input.set("empty")
    Label(app,text="Entry: ").pack()
    self.textfield=Entry(app)
    self.textfield.pack()
    Button(app,text="Enter",command=self.save_data).pack()
    l1=Label(app,textvariable=self.gui_output,height=10)
    l1.pack(side='left')
    app.mainloop()

  def save_data(self):
    data=self.textfield.get()
    if data==None:
      data="Enter"
    self.textfield.delete(0,END)
    self.gui_input.set(data)
    self.gui_output.set(x.MOME(filename,data))
    #object_1.MOME(filename,data)
    print "output " + self.gui_output.get()
  
if __name__=='__main__':
  
  filename=sys.argv[1]
  
  x=MOME(filename,"0")
  
  app_1=GUI()
