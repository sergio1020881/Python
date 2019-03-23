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
  print "inside frame"
  def __init__(self):
    print "inside frame_1"
    Frame.__init__(self)
    Frame_1.gui_input=StringVar()
    Frame_1.gui_input.set(None)
    Label(self,text="Entry: ",font=12).pack(side=LEFT,padx=10)
    #side=LEFT
    Frame_1.textfield=Entry(self)
    Frame_1.textfield.pack(side=LEFT,padx=10,pady=20)
    #side=LEFT
    l1=Label(self,textvariable=Frame_1.gui_input,height=0,font=12)
    l1.pack(side=RIGHT,padx=10)
    #side=RIGHT
    #Frame_1.textfield.insert(0,"empty")
    
#Global Methods outer scope, use only class atributes, 
#for it does not have scope to instances atributes.
def _Gui__save_data():
  Frame_1.gui_input.set(Frame_1.textfield.get())
  #print "entrada %s" % data
  if Frame_1.gui_input==None:
    Frame_1.gui_input.set("Enter")
  Frame_1.textfield.delete(0,END)
  devolver="saida -> " + Mome().mome(filename,Frame_1.gui_input.get()) #instance overflow ?
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
      return "error"
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
    Gui.problema=StringVar()
    Gui.gui_output.set(None)
    Gui.problema.set(None)
    #
    panel=Frame_1()
    panel.pack()
    
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
  
