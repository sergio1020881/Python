#!/usr/bin/python2.6 -tt
import sys
import os
import re

class MOME:
  keygen=[0,0]
  def MOME(self,mem,Input):
    if self.keygen[1]==Input:
      return self.keygen[0]
    for item in mem:
      keyfound=(item[0]==self.keygen[0] and item[1]==Input) #Bool
      if keyfound:
        #MOME UPDATE
        self.keygen[0]=item[2]
        self.keygen[1]=Input
        break
    return self.keygen[0]


if __name__=='__main__':
  object_1=MOME()
  mem=[(0,0,0),(0,1,1),(1,0,1)]
  Input=0
  x=object_1.MOME(mem,Input)
  print x
  print object_1.keygen[0]