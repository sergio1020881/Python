#!/usr/bin/python2.6 -tt
import sys
import os
import re
#import pygame.mixer
from Tkinter import *
import pygame.mixer
import sqlite3
#import pySerial

class MOME():
  keygen=[]
  inicdata="0"
  
  def __init__(self,filename,inicdata):
    self.keygen=["0","0"]
    self.MOME(filename,inicdata)
  
  def MOME(self,filename,Input):
    if self.keygen[1]==Input:
      return self.keygen[0]
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
    
def leave_func():
  exit()
    
if __name__=='__main__':
  
  filename=sys.argv[1]
  ###
  object_1=MOME(filename,"5")#create instance
  ###
  Hist='empty'
  sounds=pygame.mixer
  sounds.init()
  sound_1=sounds.Sound("wrong.wav")
  
  
  ### Window APP
  app = Tk()
  app.title("MOME")
  app.geometry('200x100+50+50')
  ### Gui Variables
  gui_input=StringVar()
  gui_input.set(None)
  #sound_1.play()
  
  gui_output=StringVar()
  gui_output.set(None)
  ###
  Label(app,text="Input: ").pack()
  
  l1=Label(app,textvariable=gui_input)
  l1.pack()
  gui_input.set(object_1.keygen[1])
  
  Label(app,text="Output: ").pack()
  
  l2=Label(app,textvariable=gui_output)
  l2.pack()
  gui_output.set(object_1.keygen[0])
  
  Button(app,text="Sair",command=leave_func).pack()
  
  ###
  while True:
    Input=raw_input("enter: ")
    gui_input.set(Input)
    if Input==Hist: #one shot
      continue
    Hist=Input
    gui_output.set(object_1.MOME(filename,Input))
    print "saida: %s" % gui_output.get()
    
  app.mainloop()
