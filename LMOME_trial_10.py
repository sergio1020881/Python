#!/usr/bin/python2.6 -tt
import sys
import os
import re
#import wx
#import cl
import pygame.mixer
from Tkinter import *
from time import sleep
#import Tkinter.messagebox

class Frame_1(Frame):
  def __init__(self):
    Frame.__init__(self)
    Frame_1.gui_input=StringVar()#class variable
    Label(self,text="Entry: ",font=12).pack(side=LEFT,padx=2,pady=2)
    #side=LEFT
    self.textfield=Entry(self)#instance variable
    self.textfield.pack(side=LEFT,padx=2,pady=2)
    #side=LEFT
    l1=Label(self,textvariable=Frame_1.gui_input,height=0,font=12)
    l1.pack(side=LEFT,padx=2)
    #side=RIGHT
    #Frame_1.textfield.insert(0,"empty")
    

class LMome:
  keygen=["0","0"]
  problema="status ok"
  def mome(self,filename,Input):
	#previne redundancia real
    if LMome.keygen[1]==Input:
      return LMome.keygen[0]
    try:
      f=open(filename,'rU')
    except Exception as causa:
      LMome.problema=causa
      print('Problema %s' % causa)
      return "error"
    for line in f:
      line=line[:-1]
      item=line.split('	')
      keyfound=(item[0]==Input) #Bool
      if keyfound:
        #MOME UPDATE
        LMome.keygen[0]=item[1]
        LMome.keygen[1]=Input
        f.close()
        break
    return LMome.keygen[0]
    
class Gui():
  def __init__(self):
    app = Tk()
    app.title("MOME")
    app.geometry('370x130+10+10')
        
    #sounds = pygame.mixer
    #sounds.init()
    #s=sounds.Sound("Weather Girls - Its Raining Men.mp3")
    #wait_finish(s.play())
    
    #Local variables
    Gui.gui_output=StringVar()
    Gui.problema=StringVar()
    Gui.gui_output.set('0')
    #Funtions
    def wait_finish(channel):
      while channel.get_busy():
        pass
    def shutdown():
      #if askokcancel(title="are you sure",message="do you realy want to quit"):
      print("Exiting program")
      sleep(1)
      app.destroy()
      #exit()
    def _Gui__save_data():
      Frame_1.gui_input.set(panel.textfield.get())
      Input=LMome.keygen[0]+":"+Frame_1.gui_input.get()#keyMOME
      print("entrada %s" % Input)
      if Frame_1.gui_input==None:
        Frame_1.gui_input.set("Enter")
      panel.textfield.delete(0,END)
      devolver="saida -> " + LMome().mome(filename,Input)#instance overflow ?
      Gui.gui_output.set(devolver)
      Gui.problema.set(LMome.problema)
      print("output %s" % Gui.gui_output.get())
    
    panel=Frame_1()
    panel.pack(side=TOP,pady=10)
    
    l1=Label(app,textvariable=Gui.gui_output,height=1,font=12)
    l1.pack(pady=10)
    #pady=2,side='left'
    l2=Label(app,textvariable=Gui.problema,height=1)
    l2.pack(side='left',pady=2)
    #side='left',pady=2
    Button(app,text="Enter",command=__save_data,width=5).pack(side='right',padx=5,pady=5)
    #side='bottom',padx=2,pady=2
    app.protocol("WM_DELETE_WINDOW",shutdown)
    app.mainloop()
  
if __name__=='__main__':
  
  filename=sys.argv[1]
  
  app_1=Gui()
