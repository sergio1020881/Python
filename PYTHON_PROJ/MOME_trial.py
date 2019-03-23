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
    #if self.keygen[1]==Input:#prevenir redundancia
      #return self.keygen[0]#aplicar em aplicacoes reais.
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
##
def save_data():
  data=textfield.get()
  if data==None:
    data="Enter"
  textfield.delete(0,END)
  gui_input.set(data)
  gui_output.set(object_1.MOME(filename,data))
  print "output " + gui_output.get()
  
if __name__=='__main__':
  
  filename=sys.argv[1]
  
  object_1=MOME(filename,"0")
  
  app = Tk()
  app.title("MOME")
  app.geometry('200x100+200+100')
  #Gui Variables
  gui_output=StringVar()
  gui_output.set(object_1.keygen[0])
  gui_input=StringVar()
  gui_input.set(object_1.keygen[1])
  
  Label(app,text="Entry: ").pack()
  
  textfield=Entry(app)
  textfield.pack()
  
  Button(app,text="Enter",command=save_data).pack()
  
  l1=Label(app,textvariable=gui_output,height=10)
  l1.pack(side='left')
  
  print "start"
    
  app.mainloop()
