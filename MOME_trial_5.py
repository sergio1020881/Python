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

#Global Methods
def _Gui__save_data():
  Gui.gui_input.set(Gui.textfield.get())
  #print "entrada %s" % data
  if Gui.gui_input==None:
    Gui.gui_input.set("Enter")
  Gui.textfield.delete(0,END)
  devolver="saida -> " + Mome().mome(filename,Gui.gui_input.get()) #instance overflow ?
  Gui.gui_output.set(devolver)
  Gui.problema.set(Mome.causa)
  print "output " + Gui.gui_output.get()

class Mome:
  keygen=["0","0"]
  causa="status ok"
  def mome(self,filename,Input):
	#previne redundancia real
    #if Mome.keygen[1]==Input:
      #return self.keygen[0]
    try:
      f=open(filename,'rU')
    except Exception as Mome.causa:
      print 'Problema %s' % Mome.causa
      return "1"
    for line in f:
      line=line[:-1]
      item=line.split('	')
      keyfound=(item[0]==Mome.keygen[0] and item[1]==Input) #Bool
      if keyfound:
        #MOME UPDATE
        Mome.keygen[0]=item[2]
        Mome.keygen[1]=Input
        f.close()
        break
    return Mome.keygen[0]
    
class Gui():
  def __init__(self):
    app = Tk()
    app.title("MOME")
    app.geometry('370x150+10+10')
    #Funtions
    def wait_finish(channel):
      while channel.get_busy():
        pass
    def shutdown():
      #if askokcancel(title="are you sure",message="do you realy want to quit"):
      print "Exiting program"
      sleep(1)
      app.destroy()
      exit()
    #Local variables
    Gui.gui_output=StringVar()
    Gui.gui_input=StringVar()
    Gui.problema=StringVar()
    Gui.gui_output.set(None)
    Gui.gui_input.set(None)
    Gui.problema.set(None)
    #
    Label(app,text="Entry: ").pack()
    #side=LEFT
    Gui.textfield=Entry(app)
    Gui.textfield.pack()
    #side=LEFT
    l3=Label(app,textvariable=Gui.gui_input,height=0)
    l3.pack()
    #side=RIGHT
    Gui.textfield.insert(0,"empty")
    l1=Label(app,textvariable=Gui.gui_output,height=0,font=12)
    l1.pack()
    #pady=2,side='left'
    l2=Label(app,textvariable=Gui.problema,height=0)
    l2.pack()
    #side='left',pady=2
    Button(app,text="Enter",command=__save_data,width=5).pack()
    #side='bottom',padx=10,pady=10
    app.protocol("WM_DELETE_WINDOW",shutdown)
    app.mainloop()
  
if __name__=='__main__':
  
  #sounds = pygame.mixer
  #sounds.init()
  #s=sounds.Sound("Stevie Wonder - I Just Called To Say I Love You.mp3")
  #wait_finish(s.play())
  
  filename=sys.argv[1]
  
  app_1=Gui()
  
