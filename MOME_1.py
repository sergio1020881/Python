#!/usr/bin/python2.6 -tt
import sys
import os
import re

class MOME:
  keygen=['0','0']
  def MOME(self,filename,Input):
    if self.keygen[1]==Input:
      return self.keygen[0]
    f=open(filename,'rU')
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
  Hist='0'
  filename='file.txt'
  while True:
    Input=raw_input("enter: ")
    if Input=='sair':
      exit()
    
    if Input==Hist: #one shot
      continue
    Hist=Input
    ###
    x=object_1.MOME(filename,Input)
    print x
      