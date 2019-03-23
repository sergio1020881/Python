#!/usr/bin/python2.6 -tt
import sys
import os
import re
#import pygame.mixer
from Tkinter import *

class MOME:
  keygen=['0','0']
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
      item=line.split(':')
      keyfound=(item[0]==self.keygen[0] and item[1]==Input) #Bool
      if keyfound:
        #MOME UPDATE
        self.keygen[0]=item[2]
        self.keygen[1]=Input
        f.close()
        break
    return self.keygen[0]
    
if __name__=='__main__':
  
  object_1=MOME()
  Hist='empty'
  ###
  app = Tk()
  app.title("MOME")
  app.geometry('200x50+50+50')
  ### Gui Variables
  gui_input=StringVar()
  gui_input.set(None)
  
  gui_output=StringVar()
  gui_output.set(None)
  ###
  filename='file.txt'
  ###
  
  Label(app,text="Output: ").pack()
  
  l1=Label(app,textvariable=gui_output)
  l1.pack()
  
  ###
  while True:
    Input=raw_input("enter: ")
    gui_input.set(Input)
    if Input=='sair':
      exit()
    if Input==Hist: #one shot
      continue
    Hist=Input
    ####
    gui_output.set(object_1.MOME(filename,Input))
    print "saida: %s" % gui_output.get()
    
  app.mainloop()
